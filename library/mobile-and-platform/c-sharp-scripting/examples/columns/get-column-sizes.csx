/*
 * Title: Get Column Sizes
 *
 * Author: Tabular Editor Community
 *
 * Description: Retrieves VertiPaq storage statistics for all columns,
 * showing which columns consume the most memory. Useful for optimization.
 *
 * Usage: Run against connected model to get column size analysis
 * CLI: te "workspace/model" samples/columns/get-column-sizes.csx --file
 *
 * Options: Modify topN variable to show more/fewer columns
 *
 * Non-interactive: Yes (works on Model object)
 */

int topN = 20;

var query = @"
TOPN(
    " + topN + @",
    SELECTCOLUMNS(
        INFO.STORAGETABLECOLUMNS(),
        ""Table"", [DIMENSION_NAME],
        ""Column"", [ATTRIBUTE_NAME],
        ""Size MB"", [DICTIONARY_SIZE] / 1024 / 1024
    ),
    [Size MB],
    DESC
)";

try {
    dynamic result = EvaluateDax(query);

    Info("=== COLUMN SIZE ANALYSIS ===");
    Info("Total Columns Analyzed: " + result.Rows.Count);
    Info("");
    Info("=== TOP " + topN + " COLUMNS BY SIZE ===");
    Info("Table.Column | Size");
    Info("".PadRight(70, '-'));

    for (int i = 0; i < result.Rows.Count; i++) {
        var table = result.Rows[i][0];
        var column = result.Rows[i][1];
        var sizeMB = Convert.ToDouble(result.Rows[i][2]).ToString("N2");
        string fullName = "[" + table + "].[" + column + "]";
        Info(fullName.PadRight(50) + " | " + sizeMB + " MB");
    }
} catch (Exception ex) {
    Error("Failed to get column sizes: " + ex.Message);
}
