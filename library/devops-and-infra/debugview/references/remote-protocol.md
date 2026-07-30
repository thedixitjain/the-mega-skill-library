# Remote Monitoring Protocol

DbgViewCli can connect to a remote machine running DbgView (GUI or service) and
receive debug output over TCP. This document describes the wire protocol.

---

## Connection

### Port Scanning

The client scans TCP ports `DBGVPORTLO` (2020) through `DBGVPORTHI` (2030) on the
target machine, attempting a connection on each until one succeeds.

| Constant | Value |
|----------|-------|
| `DBGVPORTLO` | 2020 |
| `DBGVPORTHI` | 2030 |
| Connection Timeout | 10 seconds (`REMOTE_CONNECT_TIMEOUT`) |
| Update Timeout | 30 minutes (`REMOTE_UPDATE_TIMEOUT`) |

### Connection Sequence

```
Client                              Remote Agent (DbgView)
  |                                       |
  |--- TCP connect (port 2020-2030) ----->|
  |                                       |
  |--- DBGMON_version (DWORD) ----------->|   Request version
  |<-- version (DWORD) ------------------|   Response
  |                                       |
  |--- DBGMON_hook (DWORD) -------------->|   Start kernel capture
  |--- DBGMON_swallow/dontswallow ------->|   Configure pass-through
  |--- DBGMON_forcecr/dontforcecr ------->|   Configure CR mode
  |                                       |
  |--- DBGMON_gettime (DWORD) ----------->|   Request timer resolution
  |<-- CLIENT_RESOLUTION (16 bytes) -----|   Timer resolution response
  |                                       |
  |           ... connected ...           |
```

---

## Version Handshake

After TCP connection is established:

1. Client sends `DBGMON_version` command (4 bytes, DWORD)
2. Remote responds with its driver version (4 bytes, DWORD)

### Version Interpretation

| Response Value | Meaning |
|----------------|---------|
| `DEBUGVIEW_VERSION` (0x320) | Compatible version — proceed |
| `0xFFFFFFFF & ~WIN9XVERSIONBIT` | Remote has no kernel driver loaded (Win32 only) |
| Any other value | Incompatible version — disconnect |

The high bit (`WIN9XVERSIONBIT = 0x80000000`) indicates a Windows 9x remote.

---

## Commands (Client → Remote)

All commands are sent as a single DWORD (4 bytes, little-endian).

| Command | IOCTL Value | Description |
|---------|-------------|-------------|
| `DBGMON_hook` | `CTL_CODE(0x8305, 0x00, ...)` | Start capturing kernel debug output |
| `DBGMON_unhook` | `CTL_CODE(0x8305, 0x01, ...)` | Stop capturing kernel debug output |
| `DBGMON_zerostats` | `CTL_CODE(0x8305, 0x02, ...)` | Clear output buffer |
| `DBGMON_getstats` | `CTL_CODE(0x8305, 0x03, ...)` | Request buffered output data |
| `DBGMON_swallow` | `CTL_CODE(0x8305, 0x04, ...)` | Suppress debug pass-through |
| `DBGMON_dontswallow` | `CTL_CODE(0x8305, 0x05, ...)` | Allow debug pass-through |
| `DBGMON_version` | `CTL_CODE(0x8305, 0x09, ...)` | Request version |
| `DBGMON_gettime` | `CTL_CODE(0x8305, 0x0A, ...)` | Request timer resolution |
| `DBGMON_remotequit` | `CTL_CODE(0x8305, 0x0B, ...)` | Tell remote agent to quit |
| `DBGMON_forcecr` | `CTL_CODE(0x8305, 0x0D, ...)` | Enable forced CR |
| `DBGMON_dontforcecr` | `CTL_CODE(0x8305, 0x0E, ...)` | Disable forced CR |

---

## Data Retrieval (Polling)

The client periodically requests accumulated debug output:

```
Client                              Remote Agent
  |                                       |
  |--- DBGMON_getstats (DWORD) --------->|
  |<-- STORE_BUF data (up to MAX_STORE) -|
  |                                       |
```

### Response Format

The remote sends raw `STORE_BUF.Data` content — a packed sequence of `ENTRY` records:

```c
typedef struct {
    ULONG           seq;        // Sequence number
    LARGE_INTEGER   datetime;   // File time
    LARGE_INTEGER   perftime;   // Performance counter
    char            text[0];    // Null-terminated message
} ENTRY, *PENTRY;
```

**Walking the buffer:**
```
offset = 0
while offset < bytesRead:
    entry = (ENTRY*)(buffer + offset)
    process entry->text
    offset += sizeof(ENTRY) + strlen(entry->text) + 1
```

### Timeout

The read uses a 500ms timeout. If no data arrives within that window, the client
continues its main loop (checking duration limits, exit signals, etc.).

---

## Disconnection

Graceful disconnect sequence:

```
Client                              Remote Agent
  |                                       |
  |--- DBGMON_unhook (DWORD) ----------->|   Stop capturing
  |--- DBGMON_remotequit (DWORD) ------->|   Request agent exit
  |                                       |
  |--- closesocket() ------------------->|   TCP close
```

If the connection is broken (remote closed or network error), the client detects
this via failed `ReadFile`/`WriteFile` and sets `Closing = TRUE` to prevent
further operations on that slot.

---

## Multi-Remote Support

DbgViewCli supports up to `MAXREMOTE` (10) simultaneous remote connections.
Each connection occupies a slot in the `g_ComputerInfo[MAXREMOTE]` array.

| Field | Description |
|-------|-------------|
| `Name` | Hostname or IP of the remote |
| `IpAddress` | Resolved IPv4 address (network byte order) |
| `Socket` | TCP socket handle |
| `Config` | Per-connection capture configuration |
| `NoDriver` | TRUE if remote has no kernel driver |
| `Closing` | TRUE if connection is being torn down |
| `Stats` | Allocated buffer for `DBGMON_getstats` responses |
| `ReadEvent` | Overlapped I/O event for async reads |
| `Time` | Remote's timer resolution |

---

## Security Considerations

- Remote monitoring uses **unencrypted TCP**. Do not use over untrusted networks.
- The remote agent must have DbgView running with network listening enabled.
- No authentication is performed beyond the version handshake.
- Consider using VPN or SSH tunneling for remote debug capture over WAN.
