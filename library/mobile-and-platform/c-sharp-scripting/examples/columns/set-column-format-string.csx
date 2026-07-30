/*
 * Title: Set Column Format Strings
 *
 * Description: Applies format strings to columns based on data type and
 * naming patterns. Common formats: currency, percentage, dates, numbers.
 *
 * Usage: Configure format patterns below.
 * CLI: te "workspace/model" set-column-format-string.csx --file
 *
 * Non-interactive: Yes
 */

// ============================================================================
// CONFIGURATION
// ============================================================================

var tableName = "Sales";

// Option 1: Explicit column formats
var columnFormats = new Dictionary<string, string>
{
    { "OrderDate", "mm/dd/yyyy" },
    { "ShipDate", "mm/dd/yyyy" },
    { "Revenue", "$#,##0.00" },
    { "Cost", "$#,##0.00" },
    { "UnitPrice", "$#,##0.00" },
    { "Quantity", "#,##0" },
    { "DiscountPercent", "0.00%" },
    { "MarginPercent", "0.0%" }
};

// Option 2: Pattern-based formatting (uncomment to use)
var usePatternBased = false;

// ============================================================================
// SCRIPT LOGIC
// ============================================================================

var table = Model.Tables[tableName];
var updatedCount = 0;

if(!usePatternBased)
{
    // Option 1: Explicit configuration
    foreach(var entry in columnFormats)
    {
        var columnName = entry.Key;
        var formatString = entry.Value;

        if(table.Columns.Contains(columnName))
        {
            table.Columns[columnName].FormatString = formatString;
            updatedCount++;
            Info("✓ " + columnName + " → " + formatString);
        }
        else
        {
            Info("⚠ Column not found: " + columnName);
        }
    }
}
else
{
    // Option 2: Pattern-based formatting
    foreach(var column in table.Columns)
    {
        // Skip if already has format string
        if(!string.IsNullOrEmpty(column.FormatString)) continue;

        // Date columns
        if(column.DataType == DataType.DateTime)
        {
            column.FormatString = "mm/dd/yyyy";
            updatedCount++;
        }
        // Currency columns (by name pattern)
        else if(column.Name.Contains("Revenue") ||
                column.Name.Contains("Cost") ||
                column.Name.Contains("Price") ||
                column.Name.Contains("Amount") ||
                column.Name.StartsWith("$"))
        {
            column.FormatString = "$#,##0.00";
            updatedCount++;
        }
        // Percentage columns (by name pattern)
        else if(column.Name.Contains("Percent") ||
                column.Name.Contains("Rate") ||
                column.Name.Contains("%") ||
                column.Name.EndsWith("Pct"))
        {
            column.FormatString = "0.00%";
            updatedCount++;
        }
        // Whole number columns
        else if(column.DataType == DataType.Int64)
        {
            column.FormatString = "#,##0";
            updatedCount++;
        }
        // Decimal columns (generic)
        else if(column.DataType == DataType.Decimal ||
                column.DataType == DataType.Double)
        {
            column.FormatString = "#,##0.00";
            updatedCount++;
        }
    }
}

Info("\nApplied format strings to " + updatedCount + " columns in " + tableName);

// ============================================================================
// COMMON FORMAT STRING REFERENCE
// ============================================================================

Info("\nCommon Format Strings:" +
     "\n  Currency (2 decimal):    $#,##0.00" +
     "\n  Currency (no decimal):   $#,0" +
     "\n  Percentage (2 decimal):  0.00%" +
     "\n  Percentage (1 decimal):  0.0%" +
     "\n  Percentage (no decimal): 0%" +
     "\n  Whole number:            #,##0" +
     "\n  Decimal (2 places):      #,##0.00" +
     "\n  Date (US):               mm/dd/yyyy" +
     "\n  Date (ISO):              yyyy-MM-dd" +
     "\n  Date (readable):         MMM dd, yyyy" +
     "\n  Millions/Thousands:      [>=1000000]$0.0,,\"M\";[>=1000]$0.0,\"K\";$#,0");
