# API Enable & Disable LQL Queries


## Audit API enable logs
Finds events where a Google Cloud Service API was enabled.
**Variables to replace:** None

```lql
resource.type="audited_resource" AND
protoPayload.methodName="google.api.serviceusage.v1.ServiceUsage.EnableService"
```

## Audit API disable logs
**Variables to replace:** None

```lql
resource.type="audited_resource" AND
protoPayload.methodName="google.api.serviceusage.v1.ServiceUsage.DisableService"
```

## Logging API disabled
**Variables to replace:** None

```lql
resource.type="audited_resource"
protoPayload.methodName="google.api.serviceusage.v1.ServiceUsage.DisableService"
protoPayload.authorizationInfo.granted="true"
protoPayload.response.service.state="DISABLED"
protoPayload.authorizationInfo.resource="services/logging.googleapis.com"
```
