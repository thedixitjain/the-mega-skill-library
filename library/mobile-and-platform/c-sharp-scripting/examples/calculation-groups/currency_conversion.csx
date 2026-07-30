// Example: Currency Conversion Calculation Group
// This script creates a calculation group for currency conversion

var cg = Model.AddCalculationGroup("Currency");
// Note: Precedence property only exists in TE3, not TE2

// USD (base)
var usd = cg.AddCalculationItem("USD");
usd.Expression = "SELECTEDMEASURE()";

// EUR
var eur = cg.AddCalculationItem("EUR");
eur.Expression = "SELECTEDMEASURE() * 0.85"; // Example rate

// GBP
var gbp = cg.AddCalculationItem("GBP");
gbp.Expression = "SELECTEDMEASURE() * 0.73"; // Example rate

Info("Created Currency calculation group");
