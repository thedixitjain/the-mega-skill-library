# BigQuery LQL Queries


## BigQuery audit logs
Finds audit logs related to datasets or projects.
**Variables to replace:** None

```lql
resource.type=("bigquery_dataset" OR "bigquery_project")
logName:"cloudaudit.googleapis.com"
```

## Expensive queries
Finds queries that billed more than 1GB (1073741824 bytes).
**Variables to replace:** None

```lql
resource.type="bigquery_project"
protoPayload.metadata.jobChange.job.jobStats.queryStats.totalBilledBytes > 1073741824
```

## BigQuery audit logs for a project
**Variables to replace:** None

```lql
resource.type="bigquery_project" AND
logName:"cloudaudit.googleapis.com"
```

## BigQuery audit logs for a dataset
**Variables to replace:** None

```lql
resource.type="bigquery_dataset" AND
logName:"cloudaudit.googleapis.com"
```

## BigQuery audit logs for BI Engine model
**Variables to replace:** None

```lql
resource.type="bigquery_biengine_model" AND
logName:"cloudaudit.googleapis.com"
```

## BigQuery audit logs for a Data Transfer Service run.
**Variables to replace:** None

```lql
resource.type="bigquery_dts_run" AND
logName:"cloudaudit.googleapis.com"
```

## BigQuery audit logs for a Data Transfer Service configuration.
**Variables to replace:** None

```lql
resource.type="bigquery_dts_config" AND
logName:"cloudaudit.googleapis.com"
```

## BigQuery Data Transfer Service jobs
**Variables to replace:** None

```lql
resource.type="bigquery_project" AND
protoPayload.requestMetadata.callerSuppliedUserAgent=
"BigQuery Data Transfer Service" AND
protoPayload.methodName=("google.cloud.bigquery.v2.JobService.InsertJob" OR
"google.cloud.bigquery.v2.JobService.Query")
```

## BigQuery transfer run logs
**Variables to replace:** `<CONFIG_ID>`, `<RUN_ID>`

```lql
resource.type="bigquery_dts_config" AND
labels.run_id="<RUN_ID>" AND
resource.labels.config_id="<CONFIG_ID>"
```

## BigQuery dataset updates
**Variables to replace:** None

```lql
resource.type="bigquery_dataset" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.methodName="google.cloud.bigquery.v2.DatasetService.UpdateDataset"
```

## BigQuery jobs completed
**Variables to replace:** None

```lql
resource.type="bigquery_project" AND
log_id("cloudaudit.googleapis.com/data_access") AND
protoPayload.methodName=("google.cloud.bigquery.v2.JobService.InsertJob"
OR "google.cloud.bigquery.v2.JobService.Query")
```

## BigQuery quota exceeded
**Variables to replace:** None

```lql
resource.type=("bigquery_dataset" OR "bigquery_project")
AND
protoPayload.status.code=8 AND
severity>=WARNING
```

## BigQuery query started
**Variables to replace:** None

```lql
resource.type="bigquery_project" AND
protoPayload.metadata.jobInsertion.reason:*
```

## BigQuery concurrent load/extract jobs
**Variables to replace:** None

```lql
resource.type="bigquery_resource" AND
protoPayload.methodName="jobservice.insert" AND
protoPayload.serviceData.jobInsertRequest.resource.jobConfiguration.query.query:
"extract"
```

## BigQuery audit logs for row access policy
**Variables to replace:** None

```lql
resource.type="bigquery_resource" AND
protoPayload.methodName="jobservice.insert" AND
protoPayload.serviceData.jobInsertRequest.resource.jobConfiguration.query.query:"ROW ACCESS POLICY"
```
