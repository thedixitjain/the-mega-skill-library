# explore-model.ps1
# Enumerates a PBI Desktop model's metadata hierarchically:
#   Server -> Database -> Model -> Tables -> Columns/Measures/Hierarchies/Partitions
#   + Relationships, Roles, Perspectives, Cultures, Expressions
#
# Usage: powershell.exe -NoProfile -ExecutionPolicy Bypass -File explore-model.ps1 -Port <port>

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

Write-Output "SERVER: $($server.Name)"
Write-Output "  Version: $($server.Version)"
Write-Output "  Databases: $($server.Databases.Count)"

#endregion


#region Enumerate

foreach ($db in $server.Databases) {
    Write-Output ""
    Write-Output ("=" * 70)
    Write-Output "DATABASE: $($db.Name)"
    Write-Output "  Compatibility: $($db.CompatibilityLevel)"
    Write-Output ("=" * 70)

    $model = $db.Model
    if (-not $model) { Write-Output "  (no model)"; continue }

    # Summary
    $tableCount = $model.Tables.Count
    $measureCount = ($model.Tables | ForEach-Object { $_.Measures.Count } | Measure-Object -Sum).Sum
    $relCount = $model.Relationships.Count
    Write-Output ""
    Write-Output "  MODEL SUMMARY: $tableCount tables, $measureCount measures, $relCount relationships"

    # Tables
    Write-Output ""
    Write-Output "  TABLES:"
    foreach ($table in $model.Tables) {
        $isCalcGroup = $table.CalculationGroup -ne $null
        $isCalcTable = ($table.Partitions | Where-Object { $_.SourceType -eq "Calculated" }).Count -gt 0
        $tag = ""
        if ($isCalcGroup) { $tag = " [CalcGroup]" }
        elseif ($isCalcTable) { $tag = " [CalcTable]" }
        $hidden = if ($table.IsHidden) { " [Hidden]" } else { "" }

        Write-Output ""
        Write-Output "    TABLE: [$($table.Name)]$tag$hidden"
        if ($table.Description) { Write-Output "      Desc: $($table.Description)" }
        if ($table.DataCategory) { Write-Output "      DataCategory: $($table.DataCategory)" }

        # Columns (skip RowNumberColumn -- internal engine column for VertiPaq indexing)
        $userColumns = $table.Columns | Where-Object { $_ -isnot [Microsoft.AnalysisServices.Tabular.RowNumberColumn] }
        Write-Output "      Columns ($($userColumns.Count)):"
        foreach ($col in $userColumns) {
            $colType = ""
            if ($col -is [Microsoft.AnalysisServices.Tabular.CalculatedColumn]) { $colType = " (Calc)" }
            elseif ($col -is [Microsoft.AnalysisServices.Tabular.CalculatedTableColumn]) { $colType = " (CalcTbl)" }
            $h = if ($col.IsHidden) { " [H]" } else { "" }
            $folder = if ($col.DisplayFolder) { " /$($col.DisplayFolder)" } else { "" }
            $key = if ($col.IsKey) { " [Key]" } else { "" }
            Write-Output "        [$($col.Name)] $($col.DataType)$colType$h$key$folder"
        }

        # Measures
        if ($table.Measures.Count -gt 0) {
            Write-Output "      Measures ($($table.Measures.Count)):"
            foreach ($m in $table.Measures) {
                $h = if ($m.IsHidden) { " [H]" } else { "" }
                $folder = if ($m.DisplayFolder) { " /$($m.DisplayFolder)" } else { "" }
                $fmt = if ($m.FormatString) { " Fmt='$($m.FormatString)'" } else { "" }
                $hasDRS = if ($m.DetailRowsDefinition) { " [DetailRows]" } else { "" }
                $hasFSD = if ($m.FormatStringDefinition -and $m.FormatStringDefinition.Expression) { " [DynFmt]" } else { "" }
                Write-Output "        [$($m.Name)]$h$folder$fmt$hasDRS$hasFSD"
                $expr = ($m.Expression -split "`r?`n" | Select-Object -First 3) -join " "
                if ($expr.Length -gt 120) { $expr = $expr.Substring(0, 120) + "..." }
                Write-Output "          = $expr"
            }
        }

        # Hierarchies
        if ($table.Hierarchies.Count -gt 0) {
            Write-Output "      Hierarchies ($($table.Hierarchies.Count)):"
            foreach ($h in $table.Hierarchies) {
                $levels = ($h.Levels | Sort-Object Ordinal | ForEach-Object { $_.Name }) -join " > "
                Write-Output "        [$($h.Name)]: $levels"
            }
        }

        # Calculation group items
        if ($isCalcGroup) {
            Write-Output "      Calculation Items ($($table.CalculationGroup.CalculationItems.Count)):"
            foreach ($ci in $table.CalculationGroup.CalculationItems) {
                $expr = ($ci.Expression -split "`r?`n" | Select-Object -First 1)
                if ($expr.Length -gt 100) { $expr = $expr.Substring(0, 100) + "..." }
                Write-Output "        [$($ci.Name)] Ord=$($ci.Ordinal) = $expr"
            }
        }

        # Partitions
        Write-Output "      Partitions ($($table.Partitions.Count)):"
        foreach ($p in $table.Partitions) {
            Write-Output "        [$($p.Name)] Source=$($p.SourceType) Mode=$($p.Mode)"
        }
    }

    # Relationships
    Write-Output ""
    Write-Output "  RELATIONSHIPS ($($model.Relationships.Count)):"
    foreach ($rel in $model.Relationships) {
        $sr = [Microsoft.AnalysisServices.Tabular.SingleColumnRelationship]$rel
        if ($sr) {
            $active = if ($sr.IsActive) { "Active" } else { "Inactive" }
            Write-Output "    [$($sr.FromTable.Name)].[$($sr.FromColumn.Name)] -> [$($sr.ToTable.Name)].[$($sr.ToColumn.Name)] ($($sr.FromCardinality)->$($sr.ToCardinality)) [$active] CF=$($sr.CrossFilteringBehavior)"
        }
    }

    # Roles
    if ($model.Roles.Count -gt 0) {
        Write-Output ""
        Write-Output "  ROLES ($($model.Roles.Count)):"
        foreach ($role in $model.Roles) {
            Write-Output "    [$($role.Name)] Permission=$($role.ModelPermission) Members=$($role.Members.Count)"
            foreach ($tp in $role.TablePermissions) {
                Write-Output "      Table: [$($tp.Table.Name)] Filter: $($tp.FilterExpression)"
            }
        }
    }

    # Perspectives
    if ($model.Perspectives.Count -gt 0) {
        Write-Output ""
        Write-Output "  PERSPECTIVES ($($model.Perspectives.Count)):"
        foreach ($p in $model.Perspectives) {
            Write-Output "    [$($p.Name)]"
        }
    }

    # Cultures
    if ($model.Cultures.Count -gt 0) {
        Write-Output ""
        Write-Output "  CULTURES ($($model.Cultures.Count)):"
        foreach ($c in $model.Cultures) {
            Write-Output "    [$($c.Name)] Translations=$($c.ObjectTranslations.Count)"
        }
    }

    # Expressions (shared M queries / named expressions)
    if ($model.Expressions.Count -gt 0) {
        Write-Output ""
        Write-Output "  EXPRESSIONS ($($model.Expressions.Count)):"
        foreach ($e in $model.Expressions) {
            Write-Output "    [$($e.Name)] Kind=$($e.Kind)"
        }
    }

    # Data Sources
    if ($model.DataSources.Count -gt 0) {
        Write-Output ""
        Write-Output "  DATA SOURCES ($($model.DataSources.Count)):"
        foreach ($ds in $model.DataSources) {
            $dsType = $ds.GetType().Name
            Write-Output "    [$($ds.Name)] Type=$dsType"
        }
    }
}

#endregion


#region Cleanup

$server.Disconnect()

#endregion
