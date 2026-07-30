/*
 * Title: Set Column Alignment
 *
 * Description: Sets the text alignment for columns in report visualizations.
 * Controls how text appears in table/matrix visuals.
 *
 * WHEN TO USE:
 * - Align currency values to the right for better readability
 * - Center-align headers or categorical text
 * - Left-align descriptive text fields
 * - Ensure consistent visual formatting across reports
 *
 * Usage: Configure alignments below.
 * CLI: te "workspace/model" set-alignment.csx --file
 *
 * Non-interactive: Yes
 */

// ============================================================================
// CONFIGURATION
// ============================================================================

var tableName = "Sales";

// Map: Column Name → Alignment
// Valid values: Default, Left, Right, Center
var columnAlignments = new Dictionary<string, Alignment>
{
    // Right-align numeric/currency columns
    { "Revenue", Alignment.Right },
    { "Quantity", Alignment.Right },
    { "UnitPrice", Alignment.Right },
    { "DiscountPercent", Alignment.Right },

    // Left-align text columns
    { "ProductName", Alignment.Left },
    { "CustomerName", Alignment.Left },
    { "Description", Alignment.Left },

    // Center-align dates or categorical values
    { "OrderDate", Alignment.Center },
    { "Status", Alignment.Center },
    { "Category", Alignment.Center }
};

// ============================================================================
// SCRIPT LOGIC
// ============================================================================

var table = Model.Tables[tableName];
var updatedCount = 0;

foreach(var entry in columnAlignments)
{
    var columnName = entry.Key;
    var alignment = entry.Value;

    if(table.Columns.Contains(columnName))
    {
        table.Columns[columnName].Alignment = alignment;
        updatedCount++;
        Info("✓ " + columnName + " → " + alignment);
    }
    else
    {
        Info("⚠ Column not found: " + columnName);
    }
}

Info("\nSet alignment for " + updatedCount + " columns in " + tableName);

// ============================================================================
// REFERENCE
// ============================================================================

Info("\nALIGNMENT VALUES:");
Info("  Alignment.Default - Use client default (usually left)");
Info("  Alignment.Left    - Left-align (text, descriptions)");
Info("  Alignment.Right   - Right-align (numbers, currency)");
Info("  Alignment.Center  - Center-align (dates, categories)");
