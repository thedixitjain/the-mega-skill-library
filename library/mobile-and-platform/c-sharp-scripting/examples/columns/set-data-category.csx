/*
 * Title: Set Data Category
 *
 * Description: Sets the DataCategory property for columns to enable custom
 * behaviors in Power BI. Common use cases: geographic data, images, URLs.
 *
 * Usage: Configure data categories below.
 * CLI: te "workspace/model" set-data-category.csx --file
 *
 * Non-interactive: Yes
 */

// ============================================================================
// CONFIGURATION
// ============================================================================

var tableName = "Locations";

// Map: Column Name → Data Category
// See full list: https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.datacategory
var dataCategoryMappings = new Dictionary<string, string>
{
    // Geographic categories
    { "Continent", "Continent" },
    { "Country", "Country" },
    { "StateProvince", "StateOrProvince" },
    { "City", "City" },
    { "PostalCode", "PostalCode" },
    { "County", "County" },
    { "Latitude", "Latitude" },
    { "Longitude", "Longitude" },
    { "Address", "Address" },

    // Image categories
    { "ProductImageURL", "ImageURL" },
    { "ProductImage", "Image" },

    // Web categories
    { "WebsiteURL", "WebURL" },

    // Other categories
    { "BarcodeImage", "Barcode" }
};

// ============================================================================
// SCRIPT LOGIC
// ============================================================================

var table = Model.Tables[tableName];
var updatedCount = 0;

foreach(var entry in dataCategoryMappings)
{
    var columnName = entry.Key;
    var dataCategory = entry.Value;

    if(table.Columns.Contains(columnName))
    {
        table.Columns[columnName].DataCategory = dataCategory;
        updatedCount++;
        Info("✓ " + columnName + " → " + dataCategory);
    }
    else
    {
        Info("⚠ Column not found: " + columnName);
    }
}

Info("\nSet DataCategory for " + updatedCount + " columns in " + tableName);

// ============================================================================
// COMMON DATA CATEGORY REFERENCE
// ============================================================================

Info("\nCOMMON DATA CATEGORIES:");

Info("\nGeographic:");
Info("  - Continent, Country, StateOrProvince, County");
Info("  - City, PostalCode, Address");
Info("  - Latitude, Longitude");

Info("\nImages:");
Info("  - Image, ImageURL");
Info("  - ImageBMP, ImageGIF, ImageJPG, ImagePNG, ImageTIFF");

Info("\nWeb:");
Info("  - WebURL");

Info("\nOther:");
Info("  - Barcode");
Info("  - Person, Place, Product, Organization");

Info("\nNOTE: There are 248 total data categories.");
Info("See MS-SSAS-T documentation for complete list.");

// ============================================================================
// NOTES
// ============================================================================

Info("\nUSE CASES:");
Info("- Geographic: Enables map visualizations in Power BI");
Info("- Image/ImageURL: Display images in table visuals");
Info("- WebURL: Create clickable links in reports");
Info("- Barcode: Special formatting for barcode display");
