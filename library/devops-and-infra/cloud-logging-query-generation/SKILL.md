---
name: cloud-logging-query-generation
description: ">- Generates Logging Query Language (LQL) queries for Google Cloud Logging from natural language. Use this skill when you need to query log data or when you are debugging issues. You can filter log data by Google Cloud service. Don't use this skill to query other databases, such as SQL or Spanner."
category: devops-and-infra
source_repo: google/skills
source_path: "skills/cloud/cloud-logging-query-generation/SKILL.md"
source_url: https://github.com/google/skills/blob/HEAD/skills/cloud/cloud-logging-query-generation/SKILL.md
---


# Generate Logging Query Language queries

Use this skill to generate correct Logging Query Language (LQL) queries for
Cloud Logging.

## Core rules

1.  **Strict syntax requirements:**

    *   **Always use double quotes (`"`)** for string literals. Do not use
        single quotes (`'`).
    *   Write boolean operators in all capitals: `AND`, `OR`, `NOT`.
    *   Always use parentheses to group terms and explicitly enforce precedence.

2.  **Common pitfalls:**

    *   **Instance ID vs. Instance Name:** For the `gce_instance` resource type,
        do NOT compare instance names to instance IDs. Instance names are
        strings (for example, `my-instance`). Instance IDs are numeric. If you
        only have the name, then search by instance name,
        `SEARCH("my-instance")`, or use `resource.labels.instance_name` if that
        label is available for the resource.
    *   **Resource Type Accuracy:** Do not guess resource types. You must look
        up the correct `resource.type` value in the service-specific reference
        files. For example, use `internal_http_lb_rule` for Internal HTTP(S)
        Load Balancer rules when filtering by forwarding rule name or region
        (instead of `http_load_balancer`).

3.  **Output format and placeholders:**

    *   Output **only** the raw LQL query text. Do not include conversational
        filler. Do not wrap the query in markdown code blocks unless explicitly
        requested by the user. Valid LQL comments (using `--`) are allowed, and
        are the ONLY acceptable way to include explanations or warnings.
    *   **Never block on missing variables.** If the user's request lacks
        specific identifiers (like a project ID, instance name, or IP address),
        do not ask them for clarification. Instead, insert uppercase placeholder
        strings wrapped in angle brackets (for example, `"<PROJECT_ID>"`,
        `"<YOUR_SERVICE_NAME>"`) directly into the query.

4.  **Preferred fields:**

    *   Include `resource.type` and `log_id` restrictions when the query targets
        specific Google Cloud services or resources. Global queries (for
        example, "latest error logs") do not require these restrictions.

## Detailed reference

Refer to `references/api_reference.md` for LQL syntax rules, including
Operators, NULL handling, SEARCH, and Regex.

## Service reference files

Before generating a query, you MUST read the examples for the specific service.
LQL schemas and `resource.type` values are service-specific.

**For the following services, read the exact file listed:**

*   [App Engine](references/query_app_engine.md)
*   [BigQuery](references/query_bigquery.md)
*   [Cloud Functions](references/query_cloud_functions.md)
*   [Cloud Observability (Monitoring, Logging, Trace)](references/query_cloud_observability.md)
*   [Cloud Run](references/query_cloud_run.md)
*   [Cloud Source Repositories](references/query_cloud_source_repositories.md)
*   [Cloud SQL](references/query_cloud_sql.md)
*   [Cloud Storage](references/query_cloud_storage.md)
*   [Cloud Tasks](references/query_cloud_tasks.md)
*   [Compute Engine (GCE)](references/query_compute_engine.md)
*   [Dataflow](references/query_dataflow.md)
*   [Dataproc](references/query_dataproc.md)
*   [Deployment Manager](references/query_deployment_manager.md)
*   [Kubernetes Engine (GKE)](references/query_gke.md)
*   [IAM & Service Accounts](references/query_iam.md)
*   [Networking (VPC, Load Balancing, and others)](references/query_networking.md)
*   [Security (Audit logging)](references/query_security.md)
*   [Service Usage (Enable/Disable API, Quotas)](references/query_service_usage.md)
*   [Spanner](references/query_spanner.md)
*   [Third Party (for example, Nginx, Apache)](references/query_third_party.md)

**For Google Cloud services that aren't listed:** If the service is not listed
above, write the LQL query based on your general knowledge.

## Query generation rules

1.  **Resource Types:** Explicitly define the `resource.type` in your queries
    when focusing on specific services. For some queries, you may need to search
    across multiple types (for example, `resource.type=("bigquery_project" OR
    "bigquery_dataset")`).
2.  **Audit and admin logs:** Google Cloud Audit logs (Admin Activity, Data
    Access) always follow a standard structure inside `protoPayload`. If the
    user asks for logs about who created, updated, or deleted a resource, or an
    API being called:
    *   Do NOT fall back to `SEARCH()`. Instead, use `protoPayload.methodName`.
    *   Construct the method name by guessing the service and the verb. Example:
        `protoPayload.methodName:"compute.instances.insert"`.
    *   **Always use the colon operator (`:`)** instead of equals (`=`) for
        `methodName`. The colon operator results in substring matching, which is
        the only feasible option when the exact API string isn't known.
    *   For generic API enable/disable events, use
        `resource.type="audited_resource"`.
3.  **Handling Unknown Schemas (Crucial):** If the user asks to filter by a
    specific field or condition, and if you cannot find a matching example or
    schema in the reference files, **then you must generate a query using global
    search.**
    *   Only specify `jsonPayload.*` or `protoPayload.*` field structures when
        you are certain of their exact name.
    *   Use the `SEARCH()` function to find the keyword globally within the
        correct `resource.type`.
    *   *Agent Prompt to User:* When delivering a query that uses `SEARCH`, you
        MUST add an LQL comment (using `--`) at the top of the query indicating
        you used a global keyword search because the exact schema wasn't in your
        references. Do NOT output conversational text, strictly adhere to the
        Output Format rule.

## Supporting links

*   [Cloud Logging query language documentation](https://docs.cloud.google.com/logging/docs/view/logging-query-language)
*   [Monitored resource types catalog](https://docs.cloud.google.com/logging/docs/api/v2/resource-list)
*   [Cloud Logging query library](https://docs.cloud.google.com/logging/docs/view/query-library)

---

**Source:** [`google/skills`](https://github.com/google/skills) → `skills/cloud/cloud-logging-query-generation/SKILL.md`
