/*
 * Title: Set Column Properties (Comprehensive Example)
 *
 * Description: Demonstrates how to set all common column properties including
 * DataType, SummarizeBy, FormatString, SortByColumn, IsHidden, and more.
 *
 * Usage: Modify configuration section, then run.
 * CLI: te "workspace/model" set-column-properties.csx --file
 *
 * Non-interactive: Yes
 */

// ============================================================================
// CONFIGURATION
// ============================================================================

var tableName = "Sales";

// ============================================================================
// EXAMPLE 1: Configure Key/ID Column
// ============================================================================

var customerKeyCol = Model.Tables[tableName].Columns["CustomerKey"];
customerKeyCol.DataType = DataType.Int64;
customerKeyCol.IsKey = false;  // Usually false unless it's THE primary key
customerKeyCol.IsHidden = true;
customerKeyCol.SummarizeBy = AggregateFunction.None;
customerKeyCol.DisplayFolder = "Columns/Keys";
customerKeyCol.Description = "Customer identifier (foreign key)";
customerKeyCol.IsAvailableInMDX = false;

Info("Configured CustomerKey column");

// ============================================================================
// EXAMPLE 2: Configure Date Column
// ============================================================================

var orderDateCol = Model.Tables[tableName].Columns["OrderDate"];
orderDateCol.DataType = DataType.DateTime;
orderDateCol.FormatString = "mm/dd/yyyy";
orderDateCol.SummarizeBy = AggregateFunction.None;
orderDateCol.DisplayFolder = "Columns/Dates";
orderDateCol.Description = "Date when order was placed";

Info("Configured OrderDate column");

// ============================================================================
// EXAMPLE 3: Configure Currency Column
// ============================================================================

var revenueCol = Model.Tables[tableName].Columns["Revenue"];
revenueCol.DataType = DataType.Decimal;
revenueCol.FormatString = "$#,##0.00";
revenueCol.SummarizeBy = AggregateFunction.Sum;
revenueCol.DisplayFolder = "Columns/Metrics";
revenueCol.Description = "Total revenue amount in USD";

Info("Configured Revenue column");

// ============================================================================
// EXAMPLE 4: Configure Percentage Column
// ============================================================================

var discountPctCol = Model.Tables[tableName].Columns["DiscountPercent"];
discountPctCol.DataType = DataType.Double;
discountPctCol.FormatString = "0.00%";
discountPctCol.SummarizeBy = AggregateFunction.Average;
discountPctCol.DisplayFolder = "Columns/Metrics";
discountPctCol.Description = "Discount percentage applied to order";

Info("Configured DiscountPercent column");

// ============================================================================
// EXAMPLE 5: Configure Text/Name Column
// ============================================================================

var productNameCol = Model.Tables[tableName].Columns["ProductName"];
productNameCol.DataType = DataType.String;
productNameCol.SummarizeBy = AggregateFunction.None;
productNameCol.DisplayFolder = "Columns/Names";
productNameCol.Description = "Product name from catalog";

Info("Configured ProductName column");

// ============================================================================
// EXAMPLE 6: Configure Sort By Column
// ============================================================================

// Month name sorted by month number
var monthNameCol = Model.Tables[tableName].Columns["MonthName"];
var monthNumCol = Model.Tables[tableName].Columns["MonthNumber"];

monthNameCol.DataType = DataType.String;
monthNameCol.SummarizeBy = AggregateFunction.None;
monthNameCol.SortByColumn = monthNumCol;  // Sort "Jan", "Feb" by 1, 2

monthNumCol.DataType = DataType.Int64;
monthNumCol.IsHidden = true;  // Hide the sort column
monthNumCol.SummarizeBy = AggregateFunction.None;

Info("Configured MonthName with SortByColumn");

// ============================================================================
// EXAMPLE 7: Configure Boolean/Flag Column
// ============================================================================

var isActiveCol = Model.Tables[tableName].Columns["IsActive"];
isActiveCol.DataType = DataType.Boolean;
isActiveCol.SummarizeBy = AggregateFunction.None;
isActiveCol.DisplayFolder = "Columns/Attributes";
isActiveCol.Description = "Indicates if record is currently active";

Info("Configured IsActive column");

// ============================================================================
// EXAMPLE 8: Configure Whole Number Column
// ============================================================================

var quantityCol = Model.Tables[tableName].Columns["Quantity"];
quantityCol.DataType = DataType.Int64;
quantityCol.FormatString = "#,##0";
quantityCol.SummarizeBy = AggregateFunction.Sum;
quantityCol.DisplayFolder = "Columns/Metrics";
quantityCol.Description = "Quantity of items ordered";

Info("Configured Quantity column");

// ============================================================================
// SUMMARY
// ============================================================================

Info("Column configuration complete!\n\n" +
     "Configured:\n" +
     "- Key columns (CustomerKey)\n" +
     "- Date columns (OrderDate)\n" +
     "- Currency columns (Revenue)\n" +
     "- Percentage columns (DiscountPercent)\n" +
     "- Text columns (ProductName)\n" +
     "- Sort relationships (MonthName sorted by MonthNumber)\n" +
     "- Boolean columns (IsActive)\n" +
     "- Integer columns (Quantity)");
