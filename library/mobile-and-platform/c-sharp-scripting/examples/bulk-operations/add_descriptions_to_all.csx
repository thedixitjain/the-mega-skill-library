// Example: Add Descriptions to All Objects
// This script adds default descriptions to all tables, columns, and measures

// Add descriptions to tables
foreach(var table in Model.Tables) {
    if(string.IsNullOrEmpty(table.Description)) {
        table.Description = "Table: " + table.Name;
    }
}

// Add descriptions to columns
foreach(var table in Model.Tables) {
    foreach(var column in table.Columns) {
        if(string.IsNullOrEmpty(column.Description)) {
            column.Description = column.Name + " from " + table.Name;
        }
    }
}

// Add descriptions to measures
foreach(var measure in Model.AllMeasures) {
    if(string.IsNullOrEmpty(measure.Description)) {
        measure.Description = "Measure: " + measure.Name;
    }
}

Info("Added descriptions to all objects");
