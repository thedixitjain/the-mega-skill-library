# App Engine LQL Queries



## High severity errors in a specific time range
Finds errors in a specific time range.
**Variables to replace:** `<START_TIME>`, `<END_TIME>`

```lql
resource.type="gae_app"
severity >= ERROR
timestamp >= "<START_TIME>"
timestamp <= "<END_TIME>"
```

## HTTP server errors (5xx)
Finds HTTP requests that resulted in a 5xx server error.
**Variables to replace:** None

```lql
resource.type="gae_app"
log_id("appengine.googleapis.com/request_log")
httpRequest.status >= 500
```

## App Engine logs from New Year's Eve (in UTC time)
**Variables to replace:** None

```lql
resource.type="gae_app" AND
severity>=ERROR AND
timestamp>="2025-12-31T00:00:00Z" AND timestamp<="2026-01-01T00:00:00Z"
```

## Sampled HTTP error logs
**Variables to replace:** None

```lql
resource.type="gae_app" AND
protoPayload.status >= 400 AND
sample(insertId, 0.1)
```

## App Engine log entries with a trace ID
**Variables to replace:** `<PROJECT_ID>`, `<TRACE_ID>`

```lql
resource.type="gae_app" AND
trace="projects/<PROJECT_ID>/traces/<TRACE_ID>"
```

## App Engine logs
**Variables to replace:** `<MODULE_ID>`, `<VERSION_ID>`

```lql
resource.type="gae_app" AND
resource.labels.module_id="<MODULE_ID>" AND
resource.labels.version_id="<VERSION_ID>"
```

## Log entries from App Engine deployments
**Variables to replace:** None

```lql
resource.type="gae_app" AND
protoPayload.@type="type.googleapis.com/google.cloud.audit.AuditLog" AND
protoPayload.serviceName="appengine.googleapis.com"
```

