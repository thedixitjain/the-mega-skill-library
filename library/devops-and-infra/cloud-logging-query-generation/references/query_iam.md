# IAM & Service Accounts LQL Queries



## Service account creation
Finds audit logs for the creation of new service accounts.
**Variables to replace:** None

```lql
resource.type="service_account"
log_id("cloudaudit.googleapis.com/activity")
protoPayload.methodName="google.iam.admin.v1.CreateServiceAccount"
```

## Service account creation key logs
**Variables to replace:** None

```lql
resource.type="service_account" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.methodName="google.iam.admin.v1.CreateServiceAccountKey"
```

## Set access control policy logs
**Variables to replace:** None

```lql
resource.type="project" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.methodName="SetIamPolicy"
```

## External principal granted access to organization
**Variables to replace:** `<DOMAIN_NAME>`

```lql
resource.type="project" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.@type="type.googleapis.com/google.cloud.audit.AuditLog" AND
protoPayload.request.@type:"IamPolicy" AND
protoPayload.serviceData.policyDelta.bindingDeltas.member:* AND
NOT protoPayload.serviceData.policyDelta.bindingDeltas.member:"@<DOMAIN_NAME>.com"
```

## Resource creation, modification, or deletion
**Variables to replace:** None

```lql
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.methodName:("create" OR "delete" OR "update")
```

## Role granted to principal
**Variables to replace:** `<EMAIL_ID>`

```lql
log_id("cloudaudit.googleapis.com/activity") AND
resource.type="project" AND
protoPayload.serviceName="cloudresourcemanager.googleapis.com" AND
protoPayload.methodName="SetIamPolicy" AND
protoPayload.serviceData.policyDelta.bindingDeltas.action="Add" AND
protoPayload.serviceData.policyDelta.bindingDeltas.member:"<EMAIL_ID>"
```

## Role removed from principal
**Variables to replace:** `<EMAIL_ID>`

```lql
log_id("cloudaudit.googleapis.com/activity") AND
resource.type="project" AND
protoPayload.serviceName="cloudresourcemanager.googleapis.com" AND
protoPayload.methodName="SetIamPolicy" AND
protoPayload.serviceData.policyDelta.bindingDeltas.action="Remove" AND
protoPayload.serviceData.policyDelta.bindingDeltas.member:"<EMAIL_ID>"
```

## Permission updated in a custom role
**Variables to replace:** `<ROLE_ID>`

```lql
log_id("cloudaudit.googleapis.com/activity") AND
resource.type="iam_role" AND
protoPayload.serviceName="iam.googleapis.com" AND
protoPayload.methodName:"UpdateRole" AND
resource.labels.role_name:"<ROLE_ID>"
```
