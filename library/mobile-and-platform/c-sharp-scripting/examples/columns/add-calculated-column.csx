/*
 * Title: Add Calculated Column
 *
 * Description: Creates calculated columns with DAX expressions that evaluate
 * at refresh time with row context.
 *
 * WHEN TO USE CALCULATED COLUMNS:
 * - Row-by-row calculations (Profit = Revenue - Cost)
 * - Categories/segmentation for slicing (Age bands, customer segments)
 * - Composite keys or derived keys for relationships
 * - Row-level business rules (Status based on dates)
 * - When you need to FILTER on the result
 *
 * WHEN TO USE MEASURES INSTEAD:
 * - Aggregations (SUM, AVERAGE, COUNT)
 * - Dynamic calculations based on filters
 * - Time intelligence (YTD, PY, MoM)
 * - To minimize model size (measures don't use memory)
 *
 * KEY DIFFERENCE:
 * Calculated Columns: ROW CONTEXT (can reference [Column] directly)
 * Measures: FILTER CONTEXT (must use SUM([Column]), AVERAGE([Column]), etc.)
 *
 * Usage: Configure calculated columns below.
 * CLI: te "workspace/model" add-calculated-column.csx --file
 *
 * Non-interactive: Yes
 */

// ============================================================================
// CONFIGURATION
// ============================================================================

var tableName = "Sales";

// ============================================================================
// EXAMPLE 1: Simple Row-Level Calculation
// ============================================================================

var profitCol = Model.Tables[tableName].AddCalculatedColumn("Profit");
profitCol.Expression = "[Revenue] - [Cost]";
profitCol.FormatString = "$#,##0.00";
profitCol.Description = "Profit calculated as Revenue minus Cost";
profitCol.DisplayFolder = "Calculations";
profitCol.DataType = DataType.Decimal;

Info("✓ Added: Profit (row-level calculation)");

// ============================================================================
// EXAMPLE 2: Percentage Calculation
// ============================================================================

var marginCol = Model.Tables[tableName].AddCalculatedColumn("Margin %");
marginCol.Expression = "DIVIDE([Revenue] - [Cost], [Revenue])";
marginCol.FormatString = "0.00%";
marginCol.Description = "Profit margin percentage";
marginCol.DisplayFolder = "Calculations";
marginCol.DataType = DataType.Double;

Info("✓ Added: Margin % (percentage calculation)");

// ============================================================================
// EXAMPLE 3: Category/Segmentation Column
// ============================================================================

var revenueSegmentCol = Model.Tables[tableName].AddCalculatedColumn("Revenue Segment");
revenueSegmentCol.Expression = @"
SWITCH(
    TRUE(),
    [Revenue] < 100, ""Small"",
    [Revenue] < 1000, ""Medium"",
    [Revenue] < 10000, ""Large"",
    ""Enterprise""
)";
revenueSegmentCol.DataType = DataType.String;
revenueSegmentCol.Description = "Revenue-based customer segmentation";
revenueSegmentCol.DisplayFolder = "Segments";
revenueSegmentCol.SummarizeBy = AggregateFunction.None;

Info("✓ Added: Revenue Segment (for slicing/filtering)");

// ============================================================================
// EXAMPLE 4: Conditional Logic Column
// ============================================================================

var statusCol = Model.Tables[tableName].AddCalculatedColumn("Order Status");
statusCol.Expression = @"
IF(
    ISBLANK([ShipDate]),
    ""Pending"",
    IF(
        [ShipDate] > [OrderDate] + 7,
        ""Delayed"",
        ""On Time""
    )
)";
statusCol.DataType = DataType.String;
statusCol.Description = "Order status based on ship date";
statusCol.DisplayFolder = "Attributes";
statusCol.SummarizeBy = AggregateFunction.None;

Info("✓ Added: Order Status (conditional logic)");

// ============================================================================
// EXAMPLE 5: Composite Key Column
// ============================================================================

var compositeKeyCol = Model.Tables[tableName].AddCalculatedColumn("CustomerProductKey");
compositeKeyCol.Expression = "[CustomerKey] & \"-\" & [ProductKey]";
compositeKeyCol.DataType = DataType.String;
compositeKeyCol.Description = "Composite key for Customer-Product relationships";
compositeKeyCol.IsHidden = true;
compositeKeyCol.SummarizeBy = AggregateFunction.None;

Info("✓ Added: CustomerProductKey (composite key)");

// ============================================================================
// EXAMPLE 6: Date-Based Calculation
// ============================================================================

var daysToShipCol = Model.Tables[tableName].AddCalculatedColumn("Days to Ship");
daysToShipCol.Expression = "DATEDIFF([OrderDate], [ShipDate], DAY)";
daysToShipCol.FormatString = "#,0";
daysToShipCol.DataType = DataType.Int64;
daysToShipCol.Description = "Number of days between order and shipment";
daysToShipCol.DisplayFolder = "Metrics";

Info("✓ Added: Days to Ship (date calculation)");

// ============================================================================
// SUMMARY
// ============================================================================

Info("\nAdded 6 calculated columns to " + tableName + ":");
Info("  1. Profit - Simple arithmetic");
Info("  2. Margin % - Division with DIVIDE");
Info("  3. Revenue Segment - SWITCH for categorization");
Info("  4. Order Status - Nested IF conditional logic");
Info("  5. CustomerProductKey - String concatenation for composite key");
Info("  6. Days to Ship - DATEDIFF for date math");

Info("\nREMEMBER:");
Info("  - Calculated columns use ROW CONTEXT");
Info("  - Reference columns directly: [Revenue], not SUM([Revenue])");
Info("  - Evaluated at REFRESH time (stored in model)");
Info("  - Use for slicing/filtering, not aggregation");
Info("  - Increase model size based on cardinality");
