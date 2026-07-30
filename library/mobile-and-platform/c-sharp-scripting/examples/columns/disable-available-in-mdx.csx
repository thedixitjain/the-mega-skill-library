/*
 * Title: Disable Available In MDX
 *
 * Description: Sets IsAvailableInMDX to false for specified columns.
 * This excludes columns from MDX query tools (Excel PivotTables, SSRS, etc.)
 * while keeping them available in DAX. Useful for hiding technical columns
 * from legacy MDX tools.
 *
 * Common use cases:
 * - Sort columns (MonthNumber, WeekdayNumber)
 * - Technical/system columns
 * - Helper columns not meant for end users
 *
 * Usage: Configure target columns below.
 * CLI: te "workspace/model" disable-available-in-mdx.csx --file
 *
 * Non-interactive: Yes
 */

// ============================================================================
// CONFIGURATION
// ============================================================================

// Option 1: Specify table and column names
var specificColumns = new Dictionary<string, List<string>>
{
    { "Date", new List<string> {
        "MonthNumber",
        "WeekdayNumber",
        "YearNumber",
        "QuarterNumber",
        "WeekNumber"
    }},
    { "Sales", new List<string> {
        "RowNumber",
        "SourceSystemID"
    }}
};

// Option 2: Pattern-based (uncomment to use)
var usePatternBased = false;
var patternBasedTables = new[] { "Date", "Sales", "Customers" };

// ============================================================================
// SCRIPT LOGIC - OPTION 1: SPECIFIC COLUMNS
// ============================================================================

var updatedCount = 0;

if(!usePatternBased)
{
    foreach(var tableEntry in specificColumns)
    {
        var tableName = tableEntry.Key;
        var columnNames = tableEntry.Value;

        if(!Model.Tables.Contains(tableName))
        {
            Info("⚠ Table not found: " + tableName);
            continue;
        }

        var table = Model.Tables[tableName];

        foreach(var columnName in columnNames)
        {
            if(table.Columns.Contains(columnName))
            {
                table.Columns[columnName].IsAvailableInMDX = false;
                updatedCount++;
                Info("✓ Disabled MDX: " + tableName + "[" + columnName + "]");
            }
            else
            {
                Info("⚠ Column not found: " + tableName + "[" + columnName + "]");
            }
        }
    }
}

// ============================================================================
// SCRIPT LOGIC - OPTION 2: PATTERN-BASED
// ============================================================================

else
{
    foreach(var tableName in patternBasedTables)
    {
        if(!Model.Tables.Contains(tableName))
        {
            Info("⚠ Table not found: " + tableName);
            continue;
        }

        var table = Model.Tables[tableName];

        foreach(var column in table.Columns)
        {
            // Disable MDX for hidden columns
            if(column.IsHidden)
            {
                column.IsAvailableInMDX = false;
                updatedCount++;
            }
            // Disable MDX for columns ending in "Number" (sort columns)
            else if(column.Name.EndsWith("Number") && column.DataType == DataType.Int64)
            {
                column.IsAvailableInMDX = false;
                updatedCount++;
            }
            // Disable MDX for columns ending in "ID" or "Key" (technical columns)
            else if(column.Name.EndsWith("ID") || column.Name.EndsWith("Key"))
            {
                column.IsAvailableInMDX = false;
                updatedCount++;
            }
            // Disable MDX for columns starting with "_" (system columns)
            else if(column.Name.StartsWith("_"))
            {
                column.IsAvailableInMDX = false;
                updatedCount++;
            }
        }
    }
}

Info("\nDisabled IsAvailableInMDX for " + updatedCount + " columns");

// ============================================================================
// NOTES
// ============================================================================

Info("\nNOTE:");
Info("- IsAvailableInMDX = false hides columns from Excel PivotTables and MDX tools");
Info("- Columns remain available in DAX and Power BI");
Info("- Typically used for sort columns and technical fields");
