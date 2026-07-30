/*
 * Title: Add expression to measure descriptions
 *
 * Author: Mihaly Kavasi, Ed Hansberry
 *
 * Description: Adds the DAX expression to the description of every measure
 * in the model. If a description exists, appends the expression.
 *
 * Usage: Run this script on the entire model.
 * CLI: te "workspace/model" script.csx --file
 *
 * Non-interactive: Yes (works on Model.AllMeasures)
 */

var updatedCount = 0;

foreach(var m in Model.AllMeasures)
{
    if(m.Description == "")
    {
        m.Description =  "Expression:" + "\n" + m.Expression;
        updatedCount++;
    }
    else if (!m.Description.Contains("Expression"))
    {
        m.Description = m.Description + "\n" + "Expression:" + "\n" + m.Expression;
        updatedCount++;
    }
    else
    {
        // Reset expressions already added
        int pos = m.Description.IndexOf("Expression",0);
        bool onlyExpression = (pos == 0);

        if (onlyExpression) {
            m.Description = "Expression:" + "\n" + m.Expression;
        } else {
            m.Description = m.Description.Substring(0,pos-1)  + "\n" + "Expression:" + "\n" + m.Expression;
        }
        updatedCount++;
    }
}

// Format DAX for better readability
Model.AllMeasures.FormatDax();

Info("Updated descriptions for " + updatedCount + " measures");
