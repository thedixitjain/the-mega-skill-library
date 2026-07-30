/*
 * Title: Set Column SortByColumn Property
 *
 * Description: Configures columns to sort by other columns. Common patterns:
 * - Month names sorted by month numbers
 * - Weekday names sorted by weekday numbers
 * - Custom categories sorted by order column
 *
 * Usage: Define sort relationships below.
 * CLI: te "workspace/model" set-column-sortby.csx --file
 *
 * Non-interactive: Yes
 */

// ============================================================================
// CONFIGURATION
// ============================================================================

var tableName = "Date";

// Define sort relationships: DisplayColumn → SortByColumn
var sortRelationships = new Dictionary<string, string>
{
    // Month columns
    { "MonthName", "MonthNumber" },              // "January" sorted by 1
    { "MonthShort", "MonthNumber" },             // "Jan" sorted by 1
    { "MonthYear", "YearMonth" },                // "Jan 2024" sorted by 202401

    // Weekday columns
    { "WeekdayName", "WeekdayNumber" },          // "Monday" sorted by 1
    { "WeekdayShort", "WeekdayNumber" },         // "Mon" sorted by 1

    // Quarter columns
    { "QuarterYear", "YearQuarter" },            // "Q1 2024" sorted by 202401

    // Year columns
    { "YearName", "YearNumber" },                // "2024" sorted by 2024

    // Week columns
    { "WeekLabel", "WeekNumber" }                // "Week 25" sorted by 25
};

// Auto-hide sort columns (recommended)
var hideSortColumns = true;

// ============================================================================
// SCRIPT LOGIC
// ============================================================================

var table = Model.Tables[tableName];
var updatedCount = 0;
var hiddenCount = 0;

foreach(var entry in sortRelationships)
{
    var displayColumnName = entry.Key;
    var sortColumnName = entry.Value;

    // Check both columns exist
    if(!table.Columns.Contains(displayColumnName))
    {
        Info("⚠ Display column not found: " + displayColumnName);
        continue;
    }

    if(!table.Columns.Contains(sortColumnName))
    {
        Info("⚠ Sort column not found: " + sortColumnName);
        continue;
    }

    var displayColumn = table.Columns[displayColumnName];
    var sortColumn = table.Columns[sortColumnName];

    // Set the sort relationship
    displayColumn.SortByColumn = sortColumn;
    updatedCount++;

    // Optionally hide the sort column
    if(hideSortColumns && !sortColumn.IsHidden)
    {
        sortColumn.IsHidden = true;
        sortColumn.IsAvailableInMDX = false;
        hiddenCount++;
    }

    Info("✓ " + displayColumnName + " sorted by " + sortColumnName);
}

Info("\nConfigured " + updatedCount + " sort relationships in " + tableName);
if(hideSortColumns)
{
    Info("Hidden " + hiddenCount + " sort columns");
}

// ============================================================================
// VALIDATION
// ============================================================================

Info("\nIMPORTANT: Sort column must have unique values for each display value.");
Info("Example: Each 'January' must have exactly one corresponding '1'");
