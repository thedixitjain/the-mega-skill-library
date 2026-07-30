/*
 * Title: Clean object names (CamelCase to Proper Case)
 *
 * Author: Darren Gosbell, twitter.com/DarrenGosbell
 *
 * Description: Converts CamelCaseNames to Proper Case Names by inserting
 * spaces before uppercase characters. Ignores objects with spaces already.
 * before: CalendarYearNum
 * after:  Calendar Year Num
 *
 * Usage: Run this script on the entire model.
 * CLI: te "workspace/model" script.csx --file
 *
 * Non-interactive: Yes (works on Model.Tables)
 */

// Regular expression splits on underscores and case changes
var rex = new System.Text.RegularExpressions.Regex( "(^[a-z]+|[A-Z]+(?![a-z])|[A-Z][a-z]+|[^A-Z,a-z]+|[_]|[a-z]+)");

// Table prefixes to strip (e.g., "dim", "fact", "vw")
List<string> tablePrefixesToIgnore = new List<string>() {"dim","fact", "vw","tbl","vd","td","tf","vf"};

// Table suffixes to strip (e.g., "dim", "fact")
List<string> tableSuffixesToIgnore = new List<string>() {"dim", "fact"};

var renamedTables = 0;
var renamedColumns = 0;

foreach (var tbl in Model.Tables)
{
    if (!tbl.IsHidden && !tbl.Name.Contains(" "))
    {
        string name = tbl.Name;
        var matches = rex.Matches(name);
        var firstWord = matches[0];
        var lastWord = matches[matches.Count-1];
        string[] words = matches
                        .OfType<System.Text.RegularExpressions.Match>()
                        .Where(m =>
                                m.Value != "_"
                                && !(m == firstWord && tablePrefixesToIgnore.Contains(m.Value,System.StringComparer.OrdinalIgnoreCase))
                                && !(m == lastWord && tableSuffixesToIgnore.Contains(m.Value,System.StringComparer.OrdinalIgnoreCase ))
                                )
                        .Select(m => char.ToUpper(m.Value.First()) + m.Value.Substring(1))
                        .ToArray();
        string result = string.Join(" ", words);
        tbl.Name = result;
        renamedTables++;
    }

    foreach (var col in tbl.Columns)
    {
        if (!col.IsHidden && !col.Name.Contains(" "))
        {
            string name = col.Name;
            string[] words = rex.Matches(name)
                            .OfType<System.Text.RegularExpressions.Match>()
                            .Where(m => m.Value != "_" )
                            .Select(m => char.ToUpper(m.Value.First()) + m.Value.Substring(1))
                            .ToArray();
            string result = string.Join(" ", words);
            col.Name = result;
            renamedColumns++;
        }
    }
}

Info("Renamed " + renamedTables + " tables and " + renamedColumns + " columns");
