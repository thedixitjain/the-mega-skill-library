/*
 * Title: Set Column Data Type
 *
 * Description: Sets the DataType property for columns. Use when importing
 * tables or correcting data type inference issues.
 *
 * Usage: Configure target columns and desired data types below.
 * CLI: te "workspace/model" set-column-data-type.csx --file
 *
 * Non-interactive: Yes
 */

// ============================================================================
// CONFIGURATION
// ============================================================================

var tableName = "Sales";

// Define columns and their target data types
var columnTypes = new Dictionary<string, DataType>
{
    { "CustomerKey", DataType.Int64 },
    { "OrderDate", DataType.DateTime },
    { "ShipDate", DataType.DateTime },
    { "Revenue", DataType.Decimal },
    { "Quantity", DataType.Int64 },
    { "UnitPrice", DataType.Decimal },
    { "DiscountPercent", DataType.Double },
    { "ProductName", DataType.String },
    { "IsActive", DataType.Boolean }
};

// ============================================================================
// SCRIPT LOGIC
// ============================================================================

var table = Model.Tables[tableName];
var updatedCount = 0;

foreach(var entry in columnTypes)
{
    var columnName = entry.Key;
    var dataType = entry.Value;

    if(table.Columns.Contains(columnName))
    {
        var column = table.Columns[columnName];
        column.DataType = dataType;
        updatedCount++;
        Info("Set " + columnName + " → " + dataType);
    }
    else
    {
        Info("⚠ Column not found: " + columnName);
    }
}

Info("\nUpdated data types for " + updatedCount + " columns in " + tableName);
