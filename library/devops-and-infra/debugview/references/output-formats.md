# Output Formats

DbgViewCli supports three output formats selectable via `--format <text|csv|xml>`.

---

## Text Format (Default)

Tab-separated fields written to stdout. This is the default when `--format text` or no format is specified.

### Schema

```
<sequence>\t<timestamp>\t[<pid>]\t<message>\n
```

### Fields

| Field | Description | Example |
|-------|-------------|---------|
| Sequence | Monotonically increasing line number | `1`, `2`, `3` |
| Timestamp | Depends on `--elapsed`, `--clock`, `--clock-ms` | `0.123`, `14:30:05`, `14:30:05.123` |
| PID | Process ID in brackets (when `--pids` is on) | `[1234]` |
| Message | The debug output string | `MyDriver: Init complete` |

### Timestamp Modes

| Mode | Flag | Format | Example |
|------|------|--------|---------|
| Elapsed | `--elapsed` (default) | Seconds since capture start | `12.456` |
| Clock | `--clock` | Wall clock HH:MM:SS | `14:30:05` |
| Clock+ms | `--clock-ms` | Wall clock with milliseconds | `14:30:05.123` |

### Example Output

```
1	0.000	[4567]	MyApp: Starting initialization
2	0.001	[4567]	MyApp: Loading configuration
3	0.015	[4567]	MyApp: Configuration loaded
4	1.203	[4567]	MyApp: Ready
```

---

## CSV Format

Comma-separated values with header row. Selected via `--format csv`.

### Schema

```
"Sequence","Timestamp","PID","Message"
<seq>,"<timestamp>","<pid>","<message>"
```

### Rules

- All fields are quoted with double quotes
- Embedded double quotes in message text are escaped as `""`
- Newlines in messages are preserved within quotes
- Header row is emitted first

### Example Output

```csv
"Sequence","Timestamp","PID","Message"
"1","0.000","4567","MyApp: Starting initialization"
"2","0.001","4567","MyApp: Loading configuration"
"3","0.015","4567","Config value=""debug_level=3"""
"4","1.203","4567","MyApp: Ready"
```

---

## XML Format

Simple XML elements. Selected via `--format xml`.

### Schema

```xml
<?xml version="1.0" encoding="UTF-8"?>
<debugoutput>
  <entry seq="N" time="TIMESTAMP" pid="PID"><![CDATA[MESSAGE]]></entry>
  ...
</debugoutput>
```

### Elements

| Element/Attribute | Description |
|-------------------|-------------|
| `<debugoutput>` | Root element wrapping all entries |
| `<entry>` | Single debug output line |
| `@seq` | Sequence number |
| `@time` | Timestamp string (format depends on time mode) |
| `@pid` | Process ID (omitted if `--no-pids`) |
| CDATA content | The debug message text |

### Special Characters

- Message content is wrapped in `<![CDATA[...]]>` to avoid XML escaping issues
- If the message contains the literal string `]]>`, it must be split across CDATA sections

### Example Output

```xml
<?xml version="1.0" encoding="UTF-8"?>
<debugoutput>
  <entry seq="1" time="0.000" pid="4567"><![CDATA[MyApp: Starting initialization]]></entry>
  <entry seq="2" time="0.001" pid="4567"><![CDATA[MyApp: Loading configuration]]></entry>
  <entry seq="3" time="0.015" pid="4567"><![CDATA[MyApp: Config loaded]]></entry>
  <entry seq="4" time="1.203" pid="4567"><![CDATA[MyApp: Ready]]></entry>
</debugoutput>
```

---

## Log File Options

All formats can be written to a log file simultaneously with stdout output.

| Option | Description |
|--------|-------------|
| `--log <file>` | Write output to file |
| `--log-append` | Append to existing file instead of overwriting |
| `--log-limit <MB>` | Maximum log file size in megabytes |
| `--log-wrap` | When limit reached, wrap to beginning (ring buffer) |
| `--log-daily` | Create new file each day with date suffix (e.g., `debug_20250518.log`) |

### Daily Log File Naming

When `--log-daily` is used with `--log debug.log`:
- Day 1: `debug_20250518.log`
- Day 2: `debug_20250519.log`

---

## Status Output Format

The `--status` command outputs machine-readable key=value pairs:

```
running=true
paused=false
elevated=true
```

| Key | Type | Description |
|-----|------|-------------|
| `running` | boolean | Whether a DbgViewCli instance is actively capturing |
| `paused` | boolean | Whether the running instance is paused |
| `elevated` | boolean | Whether the current process has admin privileges |
