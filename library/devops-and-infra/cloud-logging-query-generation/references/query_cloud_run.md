# Cloud Run LQL Queries


## Cloud Run logs for a specific job
**Variables to replace:** `<JOB_NAME>`

```lql
resource.type="cloud_run_job" AND
resource.labels.job_name="<JOB_NAME>"
```

## Cloud Run logs for a specific revision and service
**Variables to replace:** `<SERVICE_NAME>`

```lql
resource.type="cloud_run_revision" AND
resource.labels.service_name="<SERVICE_NAME>"
```
