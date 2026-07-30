// Example: Sync Display Folders from Measure Names
// This script organizes measures by prefix (e.g., "Sales Total" -> "Sales" folder)

foreach(var measure in Model.AllMeasures) {
    var parts = measure.Name.Split(new[] { ' ' }, 2);
    if(parts.Length > 1) {
        measure.DisplayFolder = parts[0]; // First word becomes folder
    }
}

Info("Synced display folders from measure names");
