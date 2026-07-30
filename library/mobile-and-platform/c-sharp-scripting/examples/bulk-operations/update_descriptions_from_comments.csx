// Example: Update All Measure Descriptions from Comments
// This script extracts the first comment line from measure expressions and uses it as the description

var updatedCount = 0;
foreach(var measure in Model.AllMeasures) {
    // Extract first line of expression
    var lines = measure.Expression.Split(new[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries);
    if(lines.Length > 0) {
        var firstLine = lines[0].Trim();
        // If first line is a comment, use it as description
        if(firstLine.StartsWith("//")) {
            measure.Description = firstLine.Substring(2).Trim();
            updatedCount++;
        }
    }
}

Info("Updated descriptions for " + updatedCount + " measures");
