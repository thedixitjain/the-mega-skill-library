// Example: Add Calculated Column
// This script adds a calculated column to a table

var column = Model.Tables["Sales"].AddCalculatedColumn("Profit");
column.Expression = "Sales[Revenue] - Sales[Cost]";
column.FormatString = "$#,0";
column.Description = "Calculated profit";

Info("Added calculated column: " + column.Name);
