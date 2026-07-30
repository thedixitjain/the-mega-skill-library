// Example: Initialize New Model
// This script performs common initialization tasks: hide keys, disable summarization, create base measures

// Step 1: Hide all key columns
var hiddenCount = 0;
foreach(var table in Model.Tables) {
    foreach(var column in table.Columns) {
        if(column.Name.Contains("Key") || column.Name.EndsWith("ID")) {
            column.IsHidden = true;
            hiddenCount++;
        }
        // Disable summarization for all columns
        column.SummarizeBy = AggregateFunction.None;
    }
}
Info("Step 1: Hidden " + hiddenCount + " key columns and disabled summarization");

// Step 2: Create base measures for fact tables
var sales = Model.Tables["Sales"];
var m1 = sales.AddMeasure("Total Sales", "SUM(Sales[Amount])");
m1.FormatString = "$#,0";
m1.DisplayFolder = "Base Measures";

var m2 = sales.AddMeasure("Total Quantity", "SUM(Sales[Quantity])");
m2.FormatString = "#,0";
m2.DisplayFolder = "Base Measures";

var m3 = sales.AddMeasure("Sales Count", "COUNTROWS(Sales)");
m3.FormatString = "#,0";
m3.DisplayFolder = "Base Measures";

Info("Step 2: Created 3 base measures in Sales table");

// Step 3: Create calculated measures
var m4 = sales.AddMeasure("Average Sale Amount");
m4.Expression = "DIVIDE([Total Sales], [Sales Count])";
m4.FormatString = "$#,0.00";
m4.DisplayFolder = "Calculated Measures";

Info("Step 3: Created calculated measures");
Info("Model initialization complete!");
