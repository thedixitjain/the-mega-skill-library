---
name: data-manager-api-audience-ingestion
description: ">- Guides developers through uploading audience members to Google products using the Data Manager API /v1/audienceMembers/ingest endpoint and its associated client libraries. Use this skill when the user wants to upload audience members for Customer Match, mobile device ID audiences, or any other audience use case supported by the Data Manager API. Don't use for uploading events or conversions (use the data-manager-api-event-ingestion skill)."
category: backend-and-data
source_repo: google/skills
source_path: "skills/ads/data-manager-api-audience-ingestion/SKILL.md"
source_url: https://github.com/google/skills/blob/HEAD/skills/ads/data-manager-api-audience-ingestion/SKILL.md
---

# Data Manager API Audience Ingestion

## Implementation Workflow

### Prerequisites

-   **Authentication & Library Installation**: If you need to set up access to
    the Data Manager API or install the client and utility libraries, refer to
    the `data-manager-api-setup` skill.

### Step 1: Identify Use Case & Read Documentation

-   **Determine Destination Account Type**: [CRITICAL] If it's not
    explicitly stated, STOP and CLARIFY with the user where the data is being
    sent (e.g., Google Ads, Display & Video 360, etc.) BEFORE generating any
    code. Do not assume Google Ads by default. This maps to the `account_type`
    field of the `operating_account` in the `Destination`.
-   **Read Documentation**: [CRITICAL] Follow the upload guide for
    your destination to implement the integration, as steps for configuring
    and sending the request may vary between destinations:
    *   **Google Ads Customer Match**: [Upload members to an audience](https://developers.google.com/data-manager/api/devguides/audiences/google-ads/customer-match/upload-data.md.txt)
    *   **DV360 Customer Match**: [Upload members to an audience](https://developers.google.com/data-manager/api/devguides/audiences/display-video/customer-match/upload-data.md.txt)

### Step 2: Retrieve Code Sample

> [!IMPORTANT]
> If writing or updating an ingestion script, ALWAYS retrieve the relevant code
> sample to use as a reference:

| Language | Sample |
| :--- | :--- |
| **Python** | [`ingest_audience_members.py`](https://github.com/googleads/data-manager-python/blob/main/samples/audiences/ingest_audience_members.py) |
| **Java** | [`IngestAudienceMembers.java`](https://github.com/googleads/data-manager-java/blob/main/data-manager-samples/src/main/java/com/google/ads/datamanager/samples/IngestAudienceMembers.java) |
| **PHP** | [`ingest_audience_members.php`](https://github.com/googleads/data-manager-php/blob/main/samples/audiences/ingest_audience_members.php) |
| **Node** | [`ingest_audience_members.ts`](https://github.com/googleads/data-manager-node/blob/main/samples/audiences/ingest_audience_members.ts) |
| **.NET**| [`IngestAudienceMembers.cs`](https://github.com/googleads/data-manager-dotnet/blob/main/samples/IngestAudienceMembers.cs) |

### Step 3: Retrieve Migration Guides

> [!CRITICAL]
> If refactoring code to upgrade from another Google API, ALWAYS
> extract the full contents of the relevant field mapping guide.

#### Google Ads

*   **Google Ads API Customer Match**:
    [Google Ads API to Customer Match Migration Field Mappings](https://developers.google.com/data-manager/api/devguides/audiences/google-ads/customer-match/upgrade/field-mappings.md.txt)

#### Display & Video 360

*   **Display & Video 360 API Customer Match**:
    [Display & Video 360 API to Customer Match Migration Field Mappings](https://developers.google.com/data-manager/api/devguides/audiences/display-video/customer-match/upgrade/field-mappings.md.txt)

### Step 4: Implementation

Implement the ingestion logic using the following checkpoints:

-   [ ] **Initialize Client**: Instantiate the Data Manager client
    (`IngestionServiceClient`).
-   [ ] **Define Destinations**: Build the `Destination` object using the
    `product_destination_id` and the appropriate account configurations:
    `operating_account` (target account receiving data), `login_account` (if
    authenticating using a manager account or a data partner account), and
    `linked_account` (if you're a data partner accessing the account via a
    partner link to a manager account). **STRONGLY RECOMMENDED**: Refer to
    the [Configure destinations and headers](https://developers.google.com/data-manager/api/devguides/concepts/destinations.md.txt)
    guide for more details on configuring destinations.
-   [ ] **Format User Data**: Use the utility library helpers to normalize and
    hash user identifiers correctly.
-   [ ] **Construct Payload**: Build the request payload
    (`IngestAudienceMembersRequest`) containing the destinations, formatted
    members, and consent permissions.
-   [ ] **Support Validation**: Support sending the `validate_only` boolean
    option on the `IngestAudienceMembersRequest` to allow developers to validate
    schemas without actually uploading data.
-   [ ] **Send Request**: Execute `ingest_audience_members` and record the
    returned request ID for logging/troubleshooting.
-   [ ] **Retrieve Request Status**: Check the status of the ingestion request
    using diagnostics. Since request processing is asynchronous, a
    successful ingestion response (HTTP 200 OK returning a `request_id`) only
    indicates the payload was received. To check if the records actually
    succeeded, partially succeeded, or failed to process, query
    `client.retrieve_request_status` using the `request_id`. Skipping this
    step is a common user mistake.

## Formatting

*   Fetch the [Format user data](https://developers.google.com/data-manager/api/devguides/concepts/formatting.md.txt)
    guide and use that as the source of truth for formatting and
    normalization rules.

*   Use the utility library to format, hash, and encrypt user data
    (emails, phone numbers, addresses).

    **Python Example:**
    
    ```python
    from google.ads.datamanager_util import Formatter
    from google.ads.datamanager_util.format import Encoding

    formatter: Formatter = Formatter()

    processed_email: str = formatter.process_email_address(
        email, Encoding.HEX
    )
    ```

## Critical Gotchas

*   Only set the `address` field on `UserIdentifier` if all required fields
    (`postal_code`, `family_name`, `given_name`, `region_code`) are present;
    incomplete `address` fields will cause the API request to fail.
*  `product_destination_id` must be a numeric string. It is NOT a resource
    name.
*   The enum values for `ConsentStatus` are `CONSENT_GRANTED` and
    `CONSENT_DENIED`. Do not use the values `GRANTED` and `DENIED`.
*   Field names on `UserIdentifier` are `email_address` and `phone_number`. Do
    not use the Google Ads API field names `hashed_email` and
    `hashed_phone_number`.
*   Do not call the diagnostics endpoint (`retrieve_request_status`) if
    `validate_only` is set to `true`.

## Error Handling & Troubleshooting

### Inspecting Error Payloads

> [!IMPORTANT]
> Refer to [Understand API Errors](https://developers.google.com/data-manager/api/devguides/concepts/understand-errors.md.txt)
> for a detailed guide on how to understand the structure of errors returned by
> the API.

### Retrieving Request Status (Diagnostics)

Periodically poll for status using exponential backoff, starting at least
30 minutes after sending the `IngestAudienceMembersRequest`.

1.  Call `client.retrieve_request_status` using
    `RetrieveRequestStatusRequest(request_id=...)`.
2.  Loop through `request_status_per_destination` in the response to inspect
    each target's `request_status`.
3.  If processing is complete and `request_status` is `SUCCESS`,
    `PARTIAL_SUCCESS`, or `FAILED`, inspect diagnostic values:
    *   **Audience Ingestion Status**: Check the data-type-specific status
        nested under `audience_members_ingestion_status` (for example,
        `composite_data_ingestion_status`).
        *   **Record Count**: Check `record_count` (includes both success and
            failure).
        *   **Identifier Counts**: Check the data-type-specific count field
            (e.g., `data_type_counts` for `composite_data_ingestion_status` or
            `user_identifier_count` for `user_data_ingestion_status`; see the
            [Diagnostics Guide](https://developers.google.com/data-manager/api/devguides/diagnostics.md.txt)
            for other status types).
        *   **Match Rate Range**: For `user_data` and `composite_data` uploads,
            check `upload_match_rate_range`.
    *   **Error Details**: If status is `FAILED` or `PARTIAL_SUCCESS`, inspect
        each error's `reason` and `record_count` under
        `error_info.error_counts`.
    *   **Warning Details**: Inspect each warning's `reason` and `record_count`
        under `warning_info.warning_counts` (even if the destination status is
        `SUCCESS`).

## API Reference

*   [Send audience members guide](https://developers.google.com/data-manager/api/devguides/audiences/send-audience-members.md.txt)
*   [REST API Reference](https://developers.google.com/data-manager/api/reference/rest/v1/audienceMembers/ingest.md.txt)

---

**Source:** [`google/skills`](https://github.com/google/skills) → `skills/ads/data-manager-api-audience-ingestion/SKILL.md`
