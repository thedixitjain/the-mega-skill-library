// Example: Create Measures from Column List
// This script creates SUM measures for a list of columns

var table = Model.Tables["Sales"];
var columns = new[] { "Amount", "Quantity", "Discount", "Tax", "Freight" };

foreach(var columnName in columns) {
    if(table.Columns.Contains(columnName)) {
        var measure = table.AddMeasure("Total " + columnName, "SUM(Sales[" + columnName + "])");
        measure.FormatString = "$#,0";
        measure.DisplayFolder = "Totals";
    }
}

Info("Created measures for " + columns.Length + " columns");
