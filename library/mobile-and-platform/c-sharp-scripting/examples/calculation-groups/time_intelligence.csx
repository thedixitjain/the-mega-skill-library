// Example: Create Time Intelligence Calculation Group
// This script creates a calculation group with common time intelligence patterns

Info("Creating Time Intelligence calculation group...");

// Create calculation group
var cg = Model.AddCalculationGroup("Time Intelligence");
// Note: Precedence property only exists in TE3, not TE2
cg.Description = "Time intelligence calculations for all measures";

Info("Created calculation group");

// Current Period (default)
var current = cg.AddCalculationItem("Current", "SELECTEDMEASURE()");
current.Ordinal = 0;

// Year-to-Date
var ytd = cg.AddCalculationItem("YTD");
ytd.Expression = "CALCULATE(SELECTEDMEASURE(), DATESYTD('Date'[Date]))";
ytd.Ordinal = 1;

// Month-to-Date
var mtd = cg.AddCalculationItem("MTD");
mtd.Expression = "CALCULATE(SELECTEDMEASURE(), DATESMTD('Date'[Date]))";
mtd.Ordinal = 2;

// Quarter-to-Date
var qtd = cg.AddCalculationItem("QTD");
qtd.Expression = "CALCULATE(SELECTEDMEASURE(), DATESQTD('Date'[Date]))";
qtd.Ordinal = 3;

// Prior Year
var py = cg.AddCalculationItem("PY");
py.Expression = "CALCULATE(SELECTEDMEASURE(), SAMEPERIODLASTYEAR('Date'[Date]))";
py.Ordinal = 4;

// Year-over-Year Growth %
var yoy = cg.AddCalculationItem("YoY %");
yoy.Expression = @"
VAR CurrentValue = SELECTEDMEASURE()
VAR PriorValue = CALCULATE(SELECTEDMEASURE(), SAMEPERIODLASTYEAR('Date'[Date]))
RETURN
    DIVIDE(CurrentValue - PriorValue, PriorValue)
";
yoy.Ordinal = 5;

// Month-over-Month Growth %
var mom = cg.AddCalculationItem("MoM %");
mom.Expression = @"
VAR CurrentValue = SELECTEDMEASURE()
VAR PriorValue = CALCULATE(SELECTEDMEASURE(), DATEADD('Date'[Date], -1, MONTH))
RETURN
    DIVIDE(CurrentValue - PriorValue, PriorValue)
";
mom.Ordinal = 6;

// Prior Month
var pm = cg.AddCalculationItem("PM");
pm.Expression = "CALCULATE(SELECTEDMEASURE(), DATEADD('Date'[Date], -1, MONTH))";
pm.Ordinal = 7;

// Rolling 12 Months
var r12m = cg.AddCalculationItem("R12M");
r12m.Expression = @"
CALCULATE(
    SELECTEDMEASURE(),
    DATESINPERIOD('Date'[Date], MAX('Date'[Date]), -12, MONTH)
)
";
r12m.Ordinal = 8;

Info("Created 9 time intelligence calculation items");
Info("Time Intelligence calculation group complete!");
