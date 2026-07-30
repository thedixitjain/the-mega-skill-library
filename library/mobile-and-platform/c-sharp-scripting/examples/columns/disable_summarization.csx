/*
 * Title: Disable column summarization
 *
 * Author: Tabular Editor Community
 *
 * Description: Disables automatic summarization for all columns in the model.
 * Useful when you want to force users to use explicit measures only.
 *
 * Usage: Run this script on the entire model.
 * CLI: te "workspace/model" script.csx --file
 *
 * Non-interactive: Yes (works on Model.Tables)
 */

var updatedCount = 0;

foreach(var table in Model.Tables) {
    foreach(var column in table.Columns) {
        column.SummarizeBy = AggregateFunction.None;
        updatedCount++;
    }
}

Info("Disabled summarization on " + updatedCount + " columns");
