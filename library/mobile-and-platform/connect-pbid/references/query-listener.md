# Visual Query Listener

Captures the DAX queries that Power BI Desktop sends to its embedded Analysis Services instance when visuals render — equivalent to what Performance Analyzer captures, but via DMV polling without any UI interaction.

## How It Works

PBI Desktop's embedded AS instance exposes a `DISCOVER_SESSIONS` DMV. Each session row includes a `SESSION_LAST_COMMAND` column containing the most recently executed command for that session. When a visual renders, its DAX query is sent via one of these sessions and becomes visible in this DMV.

By polling `DISCOVER_SESSIONS` repeatedly and diffing `SESSION_LAST_COMMAND` values, new visual queries can be captured in real time.

## Using the `query-listener` Agent

Dispatch the `query-listener` agent. It will:

1. Connect to the local AS instance
2. Start polling `DISCOVER_SESSIONS` every second
3. Ask you to click on visuals in the report
4. Capture and display each new DAX query as it appears
5. Stop when you signal it is done

The agent runs as a subagent with an isolated context window, so it can poll without blocking the main conversation.

## Manual Approach (PowerShell)

If you prefer to capture queries yourself:

```powershell
Add-Type -Path "$env:TEMP\tom_nuget\Microsoft.AnalysisServices.AdomdClient.retail.amd64\lib\net45\Microsoft.AnalysisServices.AdomdClient.dll"

$cmd = (Get-WmiObject Win32_Process -Filter "Name='msmdsrv.exe'").CommandLine
$portFile = [regex]::Match($cmd, '-s "([^"]+)"').Groups[1].Value + "\msmdsrv.port.txt"
$port = [System.Text.Encoding]::Unicode.GetString([System.IO.File]::ReadAllBytes($portFile)).Trim()

$conn = New-Object Microsoft.AnalysisServices.AdomdClient.AdomdConnection
$conn.ConnectionString = "Data Source=localhost:$port"
$conn.Open()

$seen = @{}
Write-Output "Listening for queries — click on visuals in Power BI Desktop..."

for ($i = 0; $i -lt 30; $i++) {
    $c = $conn.CreateCommand()
    $c.CommandText = "SELECT SESSION_ID, SESSION_LAST_COMMAND, SESSION_LAST_COMMAND_START_TIME, SESSION_LAST_COMMAND_END_TIME, SESSION_LAST_COMMAND_ELAPSED_TIME_MS, SESSION_CPU_TIME_MS FROM `$SYSTEM.DISCOVER_SESSIONS"
    $reader = $c.ExecuteReader()
    while ($reader.Read()) {
        $id  = $reader.GetValue(0).ToString()
        $cmd = $reader.GetValue(1).ToString()
        $ts  = $reader.GetValue(2).ToString()
        # Only show DAX queries (DEFINE/EVALUATE blocks), not XMLA or schema commands
        if ($cmd -match '^\s*(DEFINE|EVALUATE|VAR )' -and $seen[$id] -ne $ts) {
            $seen[$id] = $ts
            $elapsed = $reader.GetValue(5).ToString()   # SESSION_LAST_COMMAND_ELAPSED_TIME_MS
            Write-Output "`n=== Visual Query | $ts | ${elapsed}ms ==="
            Write-Output $cmd
        }
    }
    $reader.Close()
    Start-Sleep -Milliseconds 1000
}

$conn.Close()
Write-Output "Done."
```

## What to Look For

### Visual DAX queries

Visual queries start with `DEFINE` followed by `VAR` blocks and end with an `EVALUATE` and `SUMMARIZECOLUMNS` or `TOPN`. Example structure:

```dax
DEFINE
    VAR __DS0FilterTable = FILTER(...)
    VAR __DS0Core = SUMMARIZECOLUMNS(
        'Date'[Year],
        __DS0FilterTable,
        "Total Sales", [Total Sales]
    )
EVALUATE
    __DS0Core
ORDER BY ...
```

Key things to look for:

| Pattern | What it means |
|---------|---------------|
| `SUMMARIZECOLUMNS` | The main query grouping columns and measures |
| `__DS0FilterTable` | Slicers and page filters applied to the visual |
| `TOPN` wrapping `SUMMARIZECOLUMNS` | Visual has a Top N filter |
| `IGNORE(...)` | A measure that is included in grouping but not for filtering |
| `CALCULATE(...)` around a measure | Visual-level measure modification |
| `__ValueFilterDM1` | A visual-level "Value filter" (filter on a measure result) |

### Non-visual commands (ignore these)

| Pattern | Source |
|---------|--------|
| `<Subscribe ...>` | FlightRecorder/trace subscription — internal |
| `<ImageSave ...>` | PBI Desktop saving visual thumbnails |
| `<Batch ...><Discover ...>` | Schema discovery (model metadata sync) |
| `MDSCHEMA_*` | Schema rowset queries |
| `SELECT * FROM $SYSTEM.*` | DMV queries (your own polling) |

## Debugging Common Issues

**No DAX queries appear:**
- Make sure the report has visuals that need to query the model (not just slicers or cards with static text)
- Try clicking on a matrix or bar chart — these always generate queries
- Check the model isn't a thin report connected to a remote model (the local AS instance won't receive queries for thin reports)

**Queries are truncated:**
- `SESSION_LAST_COMMAND` may be truncated by the DMV. If so, extend the polling approach to capture `COMMAND_TEXT` from `DISCOVER_COMMANDS` which can be longer, but only shows active/concurrent queries.

**Queries look different from Performance Analyzer:**
- Performance Analyzer shows the query and its duration. The DMV approach captures the same data: query text from `SESSION_LAST_COMMAND`, duration from `SESSION_LAST_COMMAND_ELAPSED_TIME_MS`, and CPU time from `SESSION_CPU_TIME_MS`. Both columns are directly available in `DISCOVER_SESSIONS`.

**Same query appears multiple times:**
- This is normal — PBI Desktop re-renders visuals when filters change. Use the timestamp (`SESSION_LAST_COMMAND_START_TIME`) to deduplicate.

## Limitations

- `SESSION_LAST_COMMAND` captures the last command per session, not a history. If queries execute faster than the polling interval, intermediate queries may be missed. Use a 200-500ms poll interval for busy reports.
- Does not capture queries from thin reports connected to remote models — only local model queries are visible.
- Query text may be truncated for very large queries.
