# Driver IOCTLs and Buffer Formats

Reference documentation for the Dbgv.sys kernel driver interface used by DbgViewCli.

---

## Device Identity

| Property | Value |
|----------|-------|
| Device Type | `FILE_DEVICE_DBGMON` (`0x00008305`) |
| Driver File | `Dbgv.sys` |
| Service Name | `DBGV` |
| Registry Key | `HKLM\System\CurrentControlSet\Services\Dbgv` |
| Version | `0x320` |

---

## IOCTL Commands

All IOCTLs use `CTL_CODE(FILE_DEVICE_DBGMON, function, method, access)`.

| IOCTL Name | Function | Method | Description |
|------------|----------|--------|-------------|
| `DBGMON_hook` | `0x00` | `METHOD_BUFFERED` | Hook kernel debug output (start capturing DbgPrint) |
| `DBGMON_unhook` | `0x01` | `METHOD_BUFFERED` | Unhook kernel debug output (stop capturing) |
| `DBGMON_zerostats` | `0x02` | `METHOD_BUFFERED` | Clear the driver's internal output buffer |
| `DBGMON_getstats` | `0x03` | `METHOD_NEITHER` | Read accumulated debug output from driver buffer |
| `DBGMON_swallow` | `0x04` | `METHOD_BUFFERED` | Suppress pass-through of debug output to attached debuggers |
| `DBGMON_dontswallow` | `0x05` | `METHOD_BUFFERED` | Allow debug output to pass through to debuggers |
| `DBGMON_hookW32` | `0x06` | `METHOD_BUFFERED` | Hook Win32 debug output (session 0 global) |
| `DBGMON_unhookW32` | `0x07` | `METHOD_BUFFERED` | Unhook Win32 debug output |
| `DBGMON_getsequence` | `0x08` | `METHOD_BUFFERED` | Get current sequence number from driver |
| `DBGMON_version` | `0x09` | `METHOD_BUFFERED` | Get driver version (handshake) |
| `DBGMON_gettime` | `0x0A` | `METHOD_BUFFERED` | Get driver timer resolution |
| `DBGMON_remotequit` | `0x0B` | `METHOD_BUFFERED` | Signal remote agent to quit |
| `DBGMON_connect` | `0x0C` | `METHOD_BUFFERED` | Remote connection notification |
| `DBGMON_forcecr` | `0x0D` | `METHOD_BUFFERED` | Force carriage return on output lines |
| `DBGMON_dontforcecr` | `0x0E` | `METHOD_BUFFERED` | Don't force carriage return |
| `DBGMON_enabledbgfilter` | `0x0F` | `METHOD_BUFFERED` | Enable debug output filtering in driver |
| `DBGMON_restoredbgfilter` | `0x10` | `METHOD_BUFFERED` | Restore default debug output filtering |

---

## Buffer Structures

### STORE_BUF — Driver Output Buffer

The driver accumulates debug messages in a linked list of `STORE_BUF` pages.

```c
#define NUM_STORE_PAGES  1
#define MAX_STORE        (PAGE_SIZE * NUM_STORE_PAGES - 4 * sizeof(ULONG))
#define STORE_SIGNATURE  0xFEADDEAF

#pragma pack(1)
typedef struct _store {
    ULONG           Signature;       // Must be STORE_SIGNATURE
    ULONG           UpdateSequence;  // Incremented on each write
    struct _store * Next;            // Pointer to next buffer in chain
    ULONG           Len;             // Bytes used in Data[]
    char            Data[MAX_STORE]; // Packed ENTRY records
} STORE_BUF, *PSTORE_BUF;
#pragma pack()
```

**Size:** `STORESIZE = ((sizeof(STORE_BUF) + 0xFFF) / 0x1000)` pages

### STORE_BUF_DUMP64 — 64-bit Crash Dump Variant

For reading driver buffers from 64-bit crash dumps (pointer width differs):

```c
#pragma pack(1)
typedef struct _store_dump64 {
    ULONG           Signature;       // STORE_SIGNATURE
    ULONG           UpdateSequence;
    ULONGLONG       Next64;          // 8 bytes (64-bit kernel pointer)
    ULONG           Len;
    char            Data[MAX_STORE];
} STORE_BUF_DUMP64, *PSTORE_BUF_DUMP64;
#pragma pack()
```

### ENTRY — Individual Debug Output Record

Each entry in `Data[]` is packed sequentially:

```c
#pragma pack(1)
typedef struct {
    ULONG           seq;        // Sequence number
    LARGE_INTEGER   datetime;   // File time (100ns since 1601-01-01)
    LARGE_INTEGER   perftime;   // Performance counter value
    char            text[0];    // Null-terminated message string
} ENTRY, *PENTRY;
#pragma pack()
```

**Walking entries:** Advance by `sizeof(ENTRY) + strlen(entry->text) + 1`, aligned as needed. Validate that the next entry start does not exceed `Data + Len`.

### WIN32OUTPUT — Win32 Shared Memory Record

Used for DBWIN shared-memory capture (OutputDebugString):

```c
typedef struct _win32rec {
    struct _win32rec * next;       // Linked list pointer
    ULONG              sequence;   // Sequence number
    LARGE_INTEGER      time;       // Timestamp
    LARGE_INTEGER      perftime;   // Performance counter
    char               text[];     // Flexible array — null-terminated message
} WIN32OUTPUT, *PWIN32OUTPUT;
```

### CLIENT_RESOLUTION — Timer Resolution

Shared between service and GUI/CLI for timestamp calibration:

```c
typedef struct {
    LARGE_INTEGER   TimerResolution;
} CLIENT_RESOLUTION, *PCLIENT_RESOLUTION;
```

---

## Win32 DBWIN Shared Memory Protocol

DbgViewCli captures `OutputDebugString` by creating these named objects:

| Object Type | Name (Local Session) | Name (Global/Session 0) |
|-------------|---------------------|------------------------|
| Section (File Mapping) | `DBWIN_BUFFER` | `Global\DBWIN_BUFFER` |
| Event (buffer ready) | `DBWIN_BUFFER_READY` | `Global\DBWIN_BUFFER_READY` |
| Event (data ready) | `DBWIN_DATA_READY` | `Global\DBWIN_DATA_READY` |

**Protocol:**
1. Create the section and events with appropriate security descriptors
2. Signal `DBWIN_BUFFER_READY` to indicate buffer is available
3. Wait on `DBWIN_DATA_READY` — signaled when a process calls `OutputDebugString`
4. Read PID (first 4 bytes) + message text from the shared section
5. Signal `DBWIN_BUFFER_READY` again for the next message

---

## Boot Logging Registry Configuration

When boot logging is enabled, the driver loads at boot:

| Registry Value | Type | Data |
|----------------|------|------|
| `Start` | `REG_DWORD` | `0` (SERVICE_BOOT_START) |
| `Group` | `REG_SZ` | `System Bus Extender` |
| `Tag` | `REG_DWORD` | `1` |
| `Type` | `REG_DWORD` | `1` |
| `ImagePath` | `REG_EXPAND_SZ` | `System32\Drivers\Dbgv.sys` |

The driver binary must be copied to `%SystemRoot%\System32\Drivers\` before enabling.
