# refresh-table.ps1
# Refresh a table in Power BI Desktop via TMSL.
# Usage: powershell.exe -NoProfile -ExecutionPolicy Bypass -File refresh-table.ps1 -Port <port> -Table <table> [-Type <type>]
#
# Refresh types:
#   full       - Drop data, re-query source, recompress, recalculate DAX (default)
#   calculate  - Recalculate DAX only (no source query)
#   automatic  - Engine decides: full if never processed, otherwise calculate
#   dataOnly   - Re-query source and recompress, skip DAX recalculation
#   clearValues - Drop all data without reloading
#   defragment - Recompress existing dictionaries only
#
# Examples:
#   .\refresh-table.ps1 -Port 53706 -Table "Sales"
#   .\refresh-table.ps1 -Port 53706 -Table "Sales" -Type calculate
#   .\refresh-table.ps1 -Port 53706 -Table "ALL" -Type full

param(
    [Parameter(Mandatory=$true)]
    [int]$Port,

    [Parameter(Mandatory=$true)]
    [string]$Table,

    [ValidateSet("full", "calculate", "automatic", "dataOnly", "clearValues", "defragment")]
    [string]$Type = "full"
)


#region Setup

$basePath = "$env:TEMP\tom_nuget\Microsoft.AnalysisServices.retail.amd64\lib\net45"

if (-not (Test-Path "$basePath\Microsoft.AnalysisServices.Tabular.dll")) {
    Write-Error "TOM not installed. Run: nuget install Microsoft.AnalysisServices.retail.amd64 -OutputDirectory `$env:TEMP\tom_nuget -ExcludeVersion"
    exit 1
}

Add-Type -Path "$basePath\Microsoft.AnalysisServices.Core.dll"
Add-Type -Path "$basePath\Microsoft.AnalysisServices.Tabular.dll"

#endregion


#region Connect

$server = New-Object Microsoft.AnalysisServices.Tabular.Server
$server.Connect("Data Source=localhost:$Port")
$dbName = $server.Databases[0].Name
Write-Output "Connected to localhost:$Port"
Write-Output "Database: $dbName"

#endregion


#region Refresh

if ($Table -eq "ALL") {
    # Refresh entire database
    Write-Output "Refreshing entire model (type=$Type)..."
    $tmsl = @"
{
  "refresh": {
    "type": "$Type",
    "objects": [{ "database": "$dbName" }]
  }
}
"@
} else {
    # Refresh single table
    # Verify table exists
    if (-not $server.Databases[0].Model.Tables[$Table]) {
        Write-Error "Table '$Table' not found. Available tables:"
        foreach ($t in $server.Databases[0].Model.Tables) {
            Write-Output "  [$($t.Name)]"
        }
        $server.Disconnect()
        exit 1
    }

    Write-Output "Refreshing [$Table] (type=$Type)..."
    $tmsl = @"
{
  "refresh": {
    "type": "$Type",
    "objects": [{ "database": "$dbName", "table": "$Table" }]
  }
}
"@
}

$stopwatch = [System.Diagnostics.Stopwatch]::StartNew()

try {
    $results = $server.Execute($tmsl)
    $stopwatch.Stop()

    $hasErrors = $false
    foreach ($r in $results) {
        foreach ($msg in $r.Messages) {
            if ($msg -is [Microsoft.AnalysisServices.XmlaError]) {
                Write-Output "ERROR: $($msg.Description)"
                $hasErrors = $true
            } elseif ($msg -is [Microsoft.AnalysisServices.XmlaWarning]) {
                Write-Output "WARNING: $($msg.Description)"
            }
        }
    }

    if (-not $hasErrors) {
        Write-Output "Refresh completed in $($stopwatch.ElapsedMilliseconds) ms."
    }
} catch {
    $stopwatch.Stop()
    Write-Error "Refresh failed after $($stopwatch.ElapsedMilliseconds) ms: $($_.Exception.Message)"
}

#endregion


#region Cleanup

$server.Disconnect()

#endregion
