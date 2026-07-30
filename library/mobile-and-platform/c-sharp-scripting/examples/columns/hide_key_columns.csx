/*
 * Title: Hide key/ID columns
 *
 * Author: Tabular Editor Community
 *
 * Description: Hides all columns ending with "Key" or "ID" across
 * all tables in the model and disables summarization.
 *
 * Usage: Run this script on the entire model.
 * CLI: te "workspace/model" script.csx --file
 *
 * Non-interactive: Yes (works on Model.Tables)
 */

var hiddenCount = 0;

foreach(var table in Model.Tables) {
    foreach(var column in table.Columns) {
        if(column.Name.EndsWith("Key") || column.Name.EndsWith("ID") || column.Name.EndsWith(" ID")) {
            column.IsHidden = true;
            column.SummarizeBy = AggregateFunction.None;
            hiddenCount++;
        }
    }
}

Info("Hidden " + hiddenCount + " key/ID columns");
