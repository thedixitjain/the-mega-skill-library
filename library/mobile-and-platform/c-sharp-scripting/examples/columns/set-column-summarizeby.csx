/*
 * Title: Set Column SummarizeBy Property
 *
 * Description: Controls automatic aggregation behavior for columns in visuals.
 * Best practice: Set to None for keys, IDs, dates, and text. Use Sum only
 * for actual numeric metrics.
 *
 * Usage: Configure aggregation rules below.
 * CLI: te "workspace/model" set-column-summarizeby.csx --file
 *
 * Non-interactive: Yes
 */

// ============================================================================
// CONFIGURATION
// ============================================================================

var tableName = "Sales";

// Option 1: Set specific columns
var columnAggregations = new Dictionary<string, AggregateFunction>
{
    { "CustomerKey", AggregateFunction.None },
    { "ProductKey", AggregateFunction.None },
    { "OrderDate", AggregateFunction.None },
    { "Revenue", AggregateFunction.Sum },
    { "Quantity", AggregateFunction.Sum },
    { "DiscountPercent", AggregateFunction.Average },
    { "ProductName", AggregateFunction.None }
};

// Option 2: Pattern-based rules (uncomment to use)
var usePatternBased = false;

// ============================================================================
// SCRIPT LOGIC
// ============================================================================

var table = Model.Tables[tableName];
var updatedCount = 0;

if(!usePatternBased)
{
    // Option 1: Explicit column configuration
    foreach(var entry in columnAggregations)
    {
        var columnName = entry.Key;
        var aggregation = entry.Value;

        if(table.Columns.Contains(columnName))
        {
            table.Columns[columnName].SummarizeBy = aggregation;
            updatedCount++;
        }
    }
}
else
{
    // Option 2: Pattern-based configuration
    foreach(var column in table.Columns)
    {
        // Keys and IDs - no aggregation
        if(column.Name.EndsWith("Key") || column.Name.EndsWith("ID"))
        {
            column.SummarizeBy = AggregateFunction.None;
            updatedCount++;
        }
        // Dates - no aggregation
        else if(column.DataType == DataType.DateTime)
        {
            column.SummarizeBy = AggregateFunction.None;
            updatedCount++;
        }
        // Text - no aggregation
        else if(column.DataType == DataType.String)
        {
            column.SummarizeBy = AggregateFunction.None;
            updatedCount++;
        }
        // Boolean - no aggregation
        else if(column.DataType == DataType.Boolean)
        {
            column.SummarizeBy = AggregateFunction.None;
            updatedCount++;
        }
        // Numeric columns - check naming patterns
        else if(column.DataType == DataType.Decimal ||
                column.DataType == DataType.Double ||
                column.DataType == DataType.Int64)
        {
            // Percentages - average
            if(column.Name.Contains("Percent") || column.Name.Contains("Rate"))
            {
                column.SummarizeBy = AggregateFunction.Average;
                updatedCount++;
            }
            // Other numeric - sum
            else
            {
                column.SummarizeBy = AggregateFunction.Sum;
                updatedCount++;
            }
        }
    }
}

Info("Updated SummarizeBy for " + updatedCount + " columns in " + tableName);
