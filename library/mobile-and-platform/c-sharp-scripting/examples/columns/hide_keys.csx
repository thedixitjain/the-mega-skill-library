// Example: Hide Key Columns and Disable Summarization
// This script hides all ID/Key columns and disables summarization for all columns

Info("Starting model cleanup...");

var hiddenCount = 0;
var disabledCount = 0;

foreach(var table in Model.Tables) {
    foreach(var column in table.Columns) {
        // Disable summarization for all columns
        column.SummarizeBy = AggregateFunction.None;
        disabledCount++;

        // Hide columns that end with "Key", "ID", or start with "_"
        if(column.Name.EndsWith("Key") ||
           column.Name.EndsWith("ID") ||
           column.Name.EndsWith("Id") ||
           column.Name.StartsWith("_")) {
            column.IsHidden = true;
            hiddenCount++;
        }
    }
}

Info("Hidden " + hiddenCount + " key columns");
Info("Disabled summarization for " + disabledCount + " columns");
Info("Model cleanup complete!");
