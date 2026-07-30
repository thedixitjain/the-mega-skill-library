# modify-tom-objects.ps1
# Demonstrates TOM modification operations against a PBI Desktop model:
#   1. Create a table with explicit columns
#   2. Rename measures and set display folders / format strings
#   3. Create a new measure
#   4. Hide columns
#   5. Create a relationship
#   6. Undo all changes
#
# Usage: powershell.exe -NoProfile -ExecutionPolicy Bypass -File modify-tom-objects.ps1 -Port <port>
#
# IMPORTANT: This script modifies your model then undoes all changes.
# Review the operations before running against production models.

param(
    [Parameter(Mandatory=$true)]
    [int]$Port
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
$model = $server.Databases[0].Model

Write-Output "Connected to localhost:$Port"
Write-Output "Tables: $($model.Tables.Count), Relationships: $($model.Relationships.Count)"

#endregion


#region 1. Create a Table
# When creating tables via TOM, columns must be defined explicitly.
# PBI Desktop does NOT auto-discover columns from M expressions via TOM.
# Each DataColumn needs a SourceColumn property matching the source query output.

Write-Output ""
Write-Output "=== 1. Creating table [Session Log] with explicit columns ==="

$table = New-Object Microsoft.AnalysisServices.Tabular.Table
$table.Name = "Session Log"
$table.Description = "Tracks XP earned per session per character"

# Define columns explicitly -- SourceColumn must match the M expression output
$c1 = New-Object Microsoft.AnalysisServices.Tabular.DataColumn
$c1.Name = "Session Number"; $c1.DataType = [Microsoft.AnalysisServices.Tabular.DataType]::Int64; $c1.SourceColumn = "Session Number"
$table.Columns.Add($c1)

$c2 = New-Object Microsoft.AnalysisServices.Tabular.DataColumn
$c2.Name = "Date"; $c2.DataType = [Microsoft.AnalysisServices.Tabular.DataType]::DateTime; $c2.SourceColumn = "Date"
$table.Columns.Add($c2)

$c3 = New-Object Microsoft.AnalysisServices.Tabular.DataColumn
$c3.Name = "Character Name"; $c3.DataType = [Microsoft.AnalysisServices.Tabular.DataType]::String; $c3.SourceColumn = "Character Name"
$table.Columns.Add($c3)

$c4 = New-Object Microsoft.AnalysisServices.Tabular.DataColumn
$c4.Name = "XP Earned"; $c4.DataType = [Microsoft.AnalysisServices.Tabular.DataType]::Int64; $c4.SourceColumn = "XP Earned"
$c4.FormatString = "#,0"
$table.Columns.Add($c4)

$c5 = New-Object Microsoft.AnalysisServices.Tabular.DataColumn
$c5.Name = "Notes"; $c5.DataType = [Microsoft.AnalysisServices.Tabular.DataType]::String; $c5.SourceColumn = "Notes"
$table.Columns.Add($c5)

# Add M partition
$partition = New-Object Microsoft.AnalysisServices.Tabular.Partition
$partition.Name = "Session Log-Partition"
$partition.Source = New-Object Microsoft.AnalysisServices.Tabular.MPartitionSource
$partition.Source.Expression = 'let Source = #table({"Session Number", "Date", "Character Name", "XP Earned", "Notes"}, {{1, #date(2024,1,1), "Bob", 100, "First session"}, {2, #date(2024,1,8), "Bob", 150, "Goblin cave"}}) in Source'
$table.Partitions.Add($partition)

$model.Tables.Add($table)

#endregion


#region 2. Rename Measures + Set Display Folder + Format String

Write-Output ""
Write-Output "=== 2. Renaming measures, setting display folders and format strings ==="

# Pick two measures that exist in the model
# Adjust these names to match your model
$firstTable = $model.Tables | Where-Object { $_.Measures.Count -ge 2 } | Select-Object -First 1

if ($firstTable) {
    $measures = @($firstTable.Measures)
    $m1 = $measures[0]
    $m2 = $measures[1]

    # Save originals for undo
    $m1OrigName = $m1.Name; $m1OrigFolder = $m1.DisplayFolder; $m1OrigFmt = $m1.FormatString; $m1OrigDesc = $m1.Description
    $m2OrigName = $m2.Name; $m2OrigFolder = $m2.DisplayFolder; $m2OrigFmt = $m2.FormatString; $m2OrigDesc = $m2.Description

    # Modify
    $m1.DisplayFolder = "Measures\Key Metrics"
    $m1.Description = "Modified by modify-tom-objects.ps1"
    Write-Output "  [$($m1.Name)] -> Folder='Measures\Key Metrics'"

    $m2.DisplayFolder = "Measures\Key Metrics"
    $m2.Description = "Modified by modify-tom-objects.ps1"
    Write-Output "  [$($m2.Name)] -> Folder='Measures\Key Metrics'"
} else {
    Write-Output "  No table with 2+ measures found; skipping rename step"
}

#endregion


#region 3. Create a New Measure

Write-Output ""
Write-Output "=== 3. Creating new measure ==="

$targetTable = $model.Tables | Where-Object { $_.Measures.Count -gt 0 } | Select-Object -First 1

if ($targetTable) {
    $newMeasure = New-Object Microsoft.AnalysisServices.Tabular.Measure
    $newMeasure.Name = "_Test Measure (delete me)"
    $newMeasure.Expression = "COUNTROWS(VALUES('" + $targetTable.Name + "'))"
    $newMeasure.FormatString = "#,0"
    $newMeasure.DisplayFolder = "Measures\Test"
    $newMeasure.Description = "Test measure created by modify-tom-objects.ps1"
    $targetTable.Measures.Add($newMeasure)
    Write-Output "  Created [_Test Measure (delete me)] on [$($targetTable.Name)]"
}

#endregion


#region 4. Hide Columns

Write-Output ""
Write-Output "=== 4. Hiding columns ==="

# Hide all Int64 columns on the new table (except keys)
$hiddenCols = @()
foreach ($col in $model.Tables["Session Log"].Columns) {
    # Skip RowNumberColumn (internal engine column, not user-visible)
    if ($col -is [Microsoft.AnalysisServices.Tabular.RowNumberColumn]) { continue }
    if ($col.DataType -eq [Microsoft.AnalysisServices.Tabular.DataType]::Int64 -and $col.Name -ne "Session Number") {
        $col.IsHidden = $true
        $hiddenCols += $col.Name
    }
}
Write-Output "  Hidden on [Session Log]: $($hiddenCols -join ', ')"

#endregion


#region 5. Create a Relationship
# When creating a relationship to a newly-added table, reference the column
# objects directly (not by name lookup) and add everything in one SaveChanges() batch.

Write-Output ""
Write-Output "=== 5. Creating relationship ==="

# Find a matching column in an existing table
$existingTable = $model.Tables | Where-Object {
    $_.Columns | Where-Object { $_.Name -eq "Character Name" -and $_ -isnot [Microsoft.AnalysisServices.Tabular.RowNumberColumn] }
} | Where-Object { $_.Name -ne "Session Log" } | Select-Object -First 1

if ($existingTable) {
    $rel = New-Object Microsoft.AnalysisServices.Tabular.SingleColumnRelationship
    $rel.Name = "SessionLog_" + $existingTable.Name.Replace(" ", "")
    $rel.FromColumn = $c3  # reference the DataColumn object created earlier
    $rel.ToColumn = $existingTable.Columns["Character Name"]
    $rel.FromCardinality = [Microsoft.AnalysisServices.Tabular.RelationshipEndCardinality]::Many
    $rel.ToCardinality = [Microsoft.AnalysisServices.Tabular.RelationshipEndCardinality]::One
    $rel.IsActive = $true
    $rel.CrossFilteringBehavior = [Microsoft.AnalysisServices.Tabular.CrossFilteringBehavior]::OneDirection
    $model.Relationships.Add($rel)
    Write-Output "  [Session Log].[Character Name] -> [$($existingTable.Name)].[Character Name]"
}

#endregion


#region Save

Write-Output ""
Write-Output "=== Saving all changes ==="
$model.SaveChanges() | Out-Null
Write-Output "  Saved. Tables: $($model.Tables.Count), Relationships: $($model.Relationships.Count)"

#endregion


#region Undo

Write-Output ""
Write-Output "=== Undoing all changes ==="

# Remove relationship
if ($existingTable) {
    $relToRemove = $model.Relationships | Where-Object { $_.Name -eq "SessionLog_" + $existingTable.Name.Replace(" ", "") }
    if ($relToRemove) { $model.Relationships.Remove($relToRemove) | Out-Null }
}

# Remove test measure
if ($targetTable) {
    $testMeasure = $targetTable.Measures["_Test Measure (delete me)"]
    if ($testMeasure) { $targetTable.Measures.Remove($testMeasure) | Out-Null }
}

# Restore measure properties
if ($firstTable -and $m1) {
    $m1.DisplayFolder = $m1OrigFolder; $m1.Description = $m1OrigDesc
    $m2.DisplayFolder = $m2OrigFolder; $m2.Description = $m2OrigDesc
}

# Remove table
$sessionLog = $model.Tables["Session Log"]
if ($sessionLog) { $model.Tables.Remove($sessionLog) | Out-Null }

$model.SaveChanges() | Out-Null
Write-Output "  Restored. Tables: $($model.Tables.Count), Relationships: $($model.Relationships.Count)"

#endregion


#region Cleanup

$server.Disconnect()
Write-Output ""
Write-Output "=== Done ==="

#endregion
