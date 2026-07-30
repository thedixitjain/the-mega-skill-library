/*
 * Title: Modify Calculated Column Expression
 *
 * Description: Updates DAX expressions for existing calculated columns.
 *
 * WHEN TO USE:
 * - Fix errors in calculated column logic
 * - Update business rules embedded in columns
 * - Optimize calculated column expressions
 * - Refactor column calculations
 * - Format DAX expressions for readability
 *
 * Usage: Configure column updates below.
 * CLI: te "workspace/model" modify-calculated-column-expression.csx --file
 *
 * Non-interactive: Yes
 */

// ============================================================================
// CONFIGURATION
// ============================================================================

var tableName = "Sales";

// Map: Column Name → New Expression
var updatedExpressions = new Dictionary<string, string>
{
    // Update to use DIVIDE instead of division operator
    { "Margin %", "DIVIDE([Revenue] - [Cost], [Revenue])" },

    // Add error handling to date calculation
    { "Days to Ship", "IF(ISBLANK([ShipDate]), BLANK(), DATEDIFF([OrderDate], [ShipDate], DAY))" },

    // Refine segmentation logic
    { "Revenue Segment", @"
        SWITCH(
            TRUE(),
            [Revenue] >= 10000, ""Enterprise"",
            [Revenue] >= 1000, ""Large"",
            [Revenue] >= 100, ""Medium"",
            ""Small""
        )" },

    // Add null handling
    { "Profit", "IF(OR(ISBLANK([Revenue]), ISBLANK([Cost])), BLANK(), [Revenue] - [Cost])" }
};

// Format DAX after updating (recommended)
var formatDax = true;

// ============================================================================
// SCRIPT LOGIC
// ============================================================================

var table = Model.Tables[tableName];
var updatedCount = 0;

foreach(var entry in updatedExpressions)
{
    var columnName = entry.Key;
    var newExpression = entry.Value;

    if(!table.Columns.Contains(columnName))
    {
        Info("⚠ Column not found: " + columnName);
        continue;
    }

    var column = table.Columns[columnName];

    // Verify it's a calculated column
    if(column is CalculatedColumn)
    {
        var calcCol = column as CalculatedColumn;

        // Store old expression for logging
        var oldExpression = calcCol.Expression;

        // Update expression
        calcCol.Expression = newExpression;

        // Format if requested
        if(formatDax)
        {
            calcCol.Expression = FormatDax(calcCol.Expression);
        }

        updatedCount++;
        Info("✓ Updated: " + columnName);
        Info("  Old: " + oldExpression.Replace("\n", " ").Substring(0, Math.Min(50, oldExpression.Length)) + "...");
        Info("  New: " + newExpression.Replace("\n", " ").Substring(0, Math.Min(50, newExpression.Length)) + "...");
    }
    else
    {
        Info("⚠ Not a calculated column: " + columnName + " (type: " + column.GetType().Name + ")");
    }
}

Info("\nUpdated " + updatedCount + " calculated column expressions in " + tableName);

// ============================================================================
// BULK OPERATION: FORMAT ALL CALCULATED COLUMNS
// ============================================================================

Info("\nFormatting all calculated columns...");
var formattedCount = 0;

foreach(var column in table.Columns)
{
    if(column is CalculatedColumn)
    {
        var calcCol = column as CalculatedColumn;
        calcCol.Expression = FormatDax(calcCol.Expression);
        formattedCount++;
    }
}

Info("Formatted " + formattedCount + " calculated columns");

// ============================================================================
// NOTES
// ============================================================================

Info("\nBEST PRACTICES:");
Info("  - Use DIVIDE() instead of / to handle division by zero");
Info("  - Add ISBLANK() checks for nullable columns");
Info("  - Format DAX for readability");
Info("  - Test expressions after updating");
Info("  - Consider moving complex logic to measures if possible");
