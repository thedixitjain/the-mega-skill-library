// Example: Validate and Fix Common Issues
// This script checks for and fixes common model issues

var issues = 0;

// Check for measures without format strings
foreach(var measure in Model.AllMeasures) {
    if(string.IsNullOrEmpty(measure.FormatString)) {
        measure.FormatString = "#,0"; // Default format
        issues++;
    }
}

// Check for hidden columns that should be keys
foreach(var table in Model.Tables) {
    foreach(var column in table.Columns) {
        if(!column.IsHidden && (column.Name.EndsWith("Key") || column.Name.EndsWith("ID"))) {
            column.IsHidden = true;
            issues++;
        }
    }
}

Info("Fixed " + issues + " issues");
