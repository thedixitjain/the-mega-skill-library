# Cloud Run Functions LQL Queries



## Execution errors
Finds execution errors for Cloud Functions.
**Variables to replace:** None

```lql
resource.type="cloud_function" AND
log_id("cloudfunctions.googleapis.com/cloud-functions") AND
severity >= ERROR
```
