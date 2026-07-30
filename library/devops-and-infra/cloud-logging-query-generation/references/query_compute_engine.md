# Compute Engine (GCE) LQL Queries

## Table of Contents

- [VM Lifecycle & Audit logs](#instance-audit-logs) (L38-L72, L142-L182, L193-L205)
  - [Instance audit logs](#instance-audit-logs) (L38-L46)
  - [Syslog](#syslog) (L47-L55)
  - [VM authlogs](#compute-engine-vm-authlogs) (L65-L72)
  - [VM instance created](#compute-engine-vm-instance-created) (L142-L151)
  - [VM instance deleted](#compute-engine-vm-instance-deleted-with-name) (L152-L171)
  - [VM instance restarted](#compute-engine-vm-instance-restarted) (L172-L182)
  - [VM instance stopped by Guest OS](#compute-engine-vm-instance-stopped-by-guest-os) (L193-L205)
- [Host & Status Alerts](#compute-engine-host-error) (L73-L141, L183-L192, L206-L215)
  - [Host error](#compute-engine-host-error) (L73-L86)
  - [Host memory alert](#compute-engine-host-memory-alert) (L87-L100)
  - [Host migrated](#compute-engine-host-migrated) (L101-L116)
  - [VM terminated/preempted](#compute-engine-vm-terminatedpreempted) (L117-L126)
  - [VM terminated - scratch disk failure](#compute-engine-vm-terminated-due-to-scratch-disk-creation-failure) (L127-L141)
  - [Shielded VM integrity failure](#compute-engine-shielded-vm-boot-integrity-failure) (L183-L192)
  - [Shielded VM boot file blocked](#compute-engine-shielded-vm-boot-file-was-blocked) (L206-L215)
- [Storage, Snapshots & Sole-Tenant](#persistent-disk-created) (L216-L290)
  - [Persistent disk created](#persistent-disk-created) (L216-L225)
  - [Sole-tenant node nodes added](#nodes-added-in-sole-tenant-node) (L226-L237)
  - [Sole-tenant node autoscale events](#autoscale-events-in-sole-tenant-node) (L238-L248)
  - [Manual & scheduled snapshots](#manual-snapshot-taken) (L249-L269)
  - [Snapshot schedule creation & attachment](#snapshot-schedule-created) (L270-L290)
- [Instance Groups & Resource Limits](#quota-exceeded) (L291-L352)
  - [Quota exceeded error](#quota-exceeded) (L291-L300)
  - [Instance Group health queries](#query-unhealthy-instances-in-instance-group) (L301-L321)
  - [Instance Group membership changes](#instances-added-to-instance-group) (L322-L341)
  - [Instance template set/updated](#instance-template-set-or-updated) (L350-L352)
- [Firewall & Network](#compute-engine-firewall-rule-deletion) (L56-L64, L353-L361)
  - [Firewall rule deletion](#compute-engine-firewall-rule-deletion) (L56-L64)
  - [Firewall logs for a VM](#firewall-logs) (L353-L361)

---

## Instance audit logs
Finds activity audit logs for Compute Engine instances.
**Variables to replace:** None

```lql
resource.type="gce_instance" AND
log_id("cloudaudit.googleapis.com/activity")
```

## Syslog
Finds system logs (syslog) emitted by Compute Engine instances.
**Variables to replace:** None

```lql
resource.type="gce_instance" AND
log_id("syslog")
```

## Compute Engine firewall rule deletion
**Variables to replace:** None

```lql
resource.type="gce_firewall_rule" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.methodName:"firewalls.delete"
```

## Compute Engine VM authlogs
**Variables to replace:** None

```lql
resource.type="gce_instance" AND
log_id("authlog")
```

## Compute Engine host error
**Variables to replace:** `<INSTANCE_ID>`

```lql
resource.type="gce_instance" AND
protoPayload.serviceName="compute.googleapis.com" AND
(protoPayload.methodName:"compute.instances.hostError"
OR
operation.producer:"compute.instances.hostError") AND
log_id("cloudaudit.googleapis.com/system_event") AND
resource.labels.instance_id="<INSTANCE_ID>" AND
severity=INFO
```

## Compute Engine host memory alert
**Variables to replace:** `<INSTANCE_ID>`

```lql
resource.type="gce_instance" AND
protoPayload.serviceName="compute.googleapis.com" AND
(jsonPayload.methodName:"compute.instances.host_event_notify"
OR
operation.producer:"compute.instances.host_event_notify") AND
log_id("cloudaudit.googleapis.com/host_event_notify") AND
resource.labels.instance_id="<INSTANCE_ID>" AND
severity=CRITICAL
```

## Compute Engine host migrated
**Variables to replace:** `<INSTANCE_ID>`

```lql
resource.type="gce_instance" AND
protoPayload.serviceName="compute.googleapis.com" AND
(protoPayload.methodName:
"compute.instances.migrateOnHostMaintenance"
OR
operation.producer:
"compute.instances.migrateOnHostMaintenance") AND
log_id("cloudaudit.googleapis.com/system_event") AND
resource.labels.instance_id="<INSTANCE_ID>" AND
severity=INFO
```

## Compute Engine VM terminated/preempted
**Variables to replace:** `<INSTANCE_ID>`

```lql
resource.type="gce_instance" AND
protoPayload.methodName=~"compute\.instances\.(guestTerminate|preempted)" AND
log_id("cloudaudit.googleapis.com/system_event") AND
resource.labels.instance_id="<INSTANCE_ID>"
```

## Compute Engine VM terminated due to scratch disk creation failure
**Variables to replace:** `<INSTANCE_ID>`

```lql
resource.type="gce_instance" AND
protoPayload.serviceName="compute.googleapis.com" AND
(protoPayload.methodName="compute.instances.scratchDiskCreationFailed"
OR
operation.producer:
"compute.instances.scratchDiskCreationFailed") AND
log_id("cloudaudit.googleapis.com/system_event") AND
resource.labels.instance_id="<INSTANCE_ID>" AND
severity=INFO
```

## Compute Engine VM instance created
**Variables to replace:** `<INSTANCE_NAME>`

```lql
resource.type="gce_instance" AND
protoPayload.methodName:"compute.instances.insert" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.request.name="<INSTANCE_NAME>"
```

## Compute Engine VM instance deleted with name
**Variables to replace:** `<INSTANCE_NAME>`

```lql
resource.type="gce_instance" AND
protoPayload.methodName:"compute.instances.delete" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.resourceName:"<INSTANCE_NAME>"
```

## Compute Engine VM instance deleted with ID
**Variables to replace:** `<INSTANCE_ID>`

```lql
resource.type="gce_instance" AND
protoPayload.methodName:"compute.instances.delete" AND
log_id("cloudaudit.googleapis.com/activity") AND
resource.labels.instance_id="<INSTANCE_ID>"
```

## Compute Engine VM instance restarted
**Variables to replace:** `<INSTANCE_ID>`

```lql
resource.type="gce_instance" AND
protoPayload.methodName=~"compute\.instances\.(start|stop|reset|automaticRestart|guestTerminate|instanceManagerHaltForRestart)" AND
(log_id("cloudaudit.googleapis.com/activity")
OR log_id("cloudaudit.googleapis.com/system_event")) AND
resource.labels.instance_id="<INSTANCE_ID>"
```

## Compute Engine Shielded VM boot integrity failure
**Variables to replace:** `<INSTANCE_ID>`

```lql
resource.type="gce_instance" AND
log_id("compute.googleapis.com/shielded_vm_integrity") AND
jsonPayload.earlyBootReportEvent.policyEvaluationPassed="false" AND
resource.labels.instance_id="<INSTANCE_ID>"
```

## Compute Engine VM instance stopped by Guest OS
**Variables to replace:** `<INSTANCE_ID>`

```lql
resource.type="gce_instance" AND
protoPayload.serviceName="compute.googleapis.com" AND
(protoPayload.methodName:"compute.instances.guestTerminate" OR
operation.producer:"compute.instances.guestTerminate") AND
log_id("cloudaudit.googleapis.com/system_event") AND
resource.labels.instance_id="<INSTANCE_ID>" AND
severity=INFO
```

## Compute Engine Shielded VM boot file was blocked
**Variables to replace:** `<INSTANCE_ID>`

```lql
resource.type="gce_instance" AND
log_id("serialconsole.googleapis.com/serial_port_1_output") AND
textPayload:"Security Violation" AND
resource.labels.instance_id="<INSTANCE_ID>"
```

## Persistent Disk created
**Variables to replace:** `<PERSISTENT_DISK_NAME>`

```lql
resource.type="gce_disk" AND
protoPayload.methodName:"compute.disks.insert" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.resourceName: "<PERSISTENT_DISK_NAME>"
```

## Nodes added in sole-tenant node
**Variables to replace:** `<NODE_GROUP_ID>`

```lql
resource.type="gce_node_group" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.methodName=~("compute.nodeGroups.addNodes"
OR "compute.nodeGroups.insert") AND
resource.labels.node_group_id="<NODE_GROUP_ID>" AND
severity=INFO
```

## Autoscale events in sole-tenant node
**Variables to replace:** `<NODE_GROUP_ID>`

```lql
resource.type="gce_node_group" AND
log_id("cloudaudit.googleapis.com/system_event") AND
protoPayload.methodName=~("compute.nodeGroups.deleteNodes"
OR "compute.nodeGroups.addNodes") AND
resource.labels.node_group_id="<NODE_GROUP_ID>"
```

## Manual snapshot taken
**Variables to replace:** `<SNAPSHOT_NAME>`

```lql
resource.type="gce_snapshot" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.methodName:"compute.snapshots.insert" AND
protoPayload.resourceName:"<SNAPSHOT_NAME>"
```

## Scheduled snapshot taken
**Variables to replace:** `<PERSISTENT_DISK_NAME>`

```lql
resource.type="gce_disk" AND
log_id("cloudaudit.googleapis.com/system_event") AND
protoPayload.methodName="ScheduledSnapshots" AND
protoPayload.response.operationType="createSnapshot" AND
protoPayload.response.targetLink="<PERSISTENT_DISK_NAME>"
```

## Snapshot schedule created
**Variables to replace:** `<SCHEDULE_NAME>`

```lql
resource.type="gce_resource_policy" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.methodName:"compute.resourcePolicies.insert" AND
protoPayload.request.name="<SCHEDULE_NAME>"
```

## Snapshot schedule attached
**Variables to replace:** `<PERSISTENT_DISK_NAME>`, `<SCHEDULE_NAME>`

```lql
resource.type="gce_disk" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.methodName:"compute.disks.addResourcePolicies" AND
protoPayload.request.resourcePolicys:"<SCHEDULE_NAME>" AND
protoPayload.resourceName:"<PERSISTENT_DISK_NAME>"
```

## Quota exceeded
**Variables to replace:** None

```lql
resource.type="gce_instance" AND
protoPayload.methodName:"compute.instances.insert" AND
protoPayload.status.message:"QUOTA_EXCEEDED" AND
severity=ERROR
```

## Query unhealthy instances in instance group
**Variables to replace:** `<INSTANCE_GROUP_NAME>`

```lql
resource.type="gce_instance_group" AND
resource.labels.instance_group_name="<INSTANCE_GROUP_NAME>" AND
jsonPayload.healthCheckProbeResult.healthState="UNHEALTHY"
```

## Query instance group members within a time frame in UTC time format
**Variables to replace:** `<END_TIME>`, `<INSTANCE_GROUP_NAME>`, `<START_TIME>`

```lql
resource.type="gce_instance_group_manager" AND
resource.labels.instance_group_manager_name="<INSTANCE_GROUP_NAME>" AND
jsonPayload.@type=
"type.googleapis.com/compute.InstanceGroupManagerEvent" AND
jsonPayload.instanceHealthStateChange.detailedHealthState="HEALTHY" AND
timestamp >= "<START_TIME>" AND timestamp <= "<END_TIME>"
```

## Instances added to instance group
**Variables to replace:** `<INSTANCE_GROUP_NAME>`

```lql
resource.type="gce_instance_group" AND
protoPayload.methodName:"compute.instanceGroups.addInstances" AND
log_id("cloudaudit.googleapis.com/activity") AND
resource.labels.instance_group_name="<INSTANCE_GROUP_NAME>"
```

## Instances removed from instance group
**Variables to replace:** `<INSTANCE_GROUP_NAME>`

```lql
resource.type="gce_instance_group" AND
protoPayload.methodName:"compute.instanceGroups.removeInstances" AND
log_id("cloudaudit.googleapis.com/activity") AND
resource.labels.instance_group_name="<INSTANCE_GROUP_NAME>"
```

## Instance template set or updated
**Variables to replace:** `<INSTANCE_GROUP_MANAGER>`

```lql
resource.type="gce_instance_group_manager" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.methodName=
"v1.compute.instanceGroupManagers.setInstanceTemplate" AND
resource.labels.instance_group_manager_name="<INSTANCE_GROUP_MANAGER>"
```

## Firewall logs
**Variables to replace:** `<INSTANCE_NAME>`

```lql
resource.type="gce_subnetwork" AND
log_id("compute.googleapis.com/firewall") AND
jsonPayload.instance.vm_name="<INSTANCE_NAME>"
```
