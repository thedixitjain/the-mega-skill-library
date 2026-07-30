# Cloud Storage (GCS) LQL Queries


## GCS bucket audit logs
Finds all audit logs for Cloud Storage buckets.
**Variables to replace:** None

```lql
resource.type="gcs_bucket" AND
logName:"cloudaudit.googleapis.com"
```

## GCS bucket deletion events
Finds activity logs for bucket deletion.
**Variables to replace:** None

```lql
resource.type="gcs_bucket" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.methodName="storage.buckets.delete"
```

## GCS bucket logs
**Variables to replace:** `<BUCKET_NAME>`

```lql
resource.type="gcs_bucket" AND
resource.labels.bucket_name="<BUCKET_NAME>"
```

## GCS bucket creation logs
**Variables to replace:** None

```lql
resource.type="gcs_bucket" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.methodName="storage.buckets.create"
```

