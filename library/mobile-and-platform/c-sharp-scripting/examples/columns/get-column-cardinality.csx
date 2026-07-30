/*
 * Title: Get Column Cardinality
 *
 * Author: Tabular Editor Community
 *
 * Description: Retrieves cardinality (distinct value count) for columns.
 * High cardinality columns can impact model size and query performance.
 *
 * Usage: Run on selected columns or all columns in model
 * CLI: te "workspace/model" samples/columns/get-column-cardinality.csx --file
 *
 * Options:
 * - Set useSelection = true to analyze only selected columns
 * - Set topN to control how many high-cardinality columns to show
 *
 * Non-interactive: Works on Selected.Columns or Model.AllColumns
 */

bool useSelection = false; // Set to true to analyze only selected columns
int topN = 20; // Number of top columns to display

var columnsToAnalyze = useSelection ? Selected.Columns : Model.AllColumns;

if (!columnsToAnalyze.Any()) {
    Error("No columns to analyze. Select columns or set useSelection = false");
}
else {
    Info("Analyzing cardinality for " + columnsToAnalyze.Count() + " columns...");

    var cardinalityStats = new List<Tuple<string, string, long, string>>();

    foreach(var column in columnsToAnalyze.Where(c => c.Type != ColumnType.RowNumber)) {
    try {
        string dax = "COUNTROWS(DISTINCT(" + column.DaxObjectFullName + "))";
        dynamic result = EvaluateDax(dax);

        long cardinality = 0;
        if (result != null && long.TryParse(result.ToString(), out cardinality)) {
            cardinalityStats.Add(Tuple.Create(
                column.Table.Name,
                column.Name,
                cardinality,
                column.DataType.ToString()
            ));
        }
    } catch (Exception ex) {
        Error("Failed to get cardinality for [" + column.Table.Name + "].[" + column.Name + "]: " + ex.Message);
    }
    }

    // Sort by cardinality (highest first)
    var sortedByCardinality = cardinalityStats.OrderByDescending(c => c.Item3).ToList();

    // Output results
    Info("");
    Info("=== COLUMN CARDINALITY ANALYSIS ===");
    Info("Analyzed Columns: " + cardinalityStats.Count);
    Info("");
    Info("=== TOP " + topN + " COLUMNS BY CARDINALITY ===");
    Info("Table.Column | Cardinality | Data Type");
    Info("".PadRight(70, '-'));

    foreach(var column in sortedByCardinality.Take(topN)) {
        string fullName = "[" + column.Item1 + "].[" + column.Item2 + "]";
        Info(fullName.PadRight(40) + " | " + column.Item3.ToString("N0").PadLeft(12) + " | " + column.Item4);
    }
}
