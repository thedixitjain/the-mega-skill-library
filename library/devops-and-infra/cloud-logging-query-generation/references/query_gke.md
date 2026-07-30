# Kubernetes Engine (GKE) LQL Queries

## Table of Contents

- [Cluster & Container Basics](#cluster-logs-in-a-specific-location) (L50-L78, L132-L139, L167-L175, L265-L273, L374-L492, L523-L579)
  - [Cluster logs by location](#cluster-logs-in-a-specific-location) (L50-L58)
  - [Pod eviction events](#pod-eviction-events) (L59-L68)
  - [Container errors](#container-errors) (L69-L78)
  - [Kubernetes events (overview)](#kubernetes-events) (L132-L139)
  - [Pod deletion](#pod-deletion) (L167-L175)
  - [Query pod during creation](#query-pod-during-creation) (L265-L273)
  - [Stdout/stderr container logs (overview)](#stdout-container-logs-across-all-pods-and-containers-in-a-cluster) (L374-L390)
  - [Container logs by specific name/container/namespace](#container-error-logs-for-a-pod-with-a-specific-name) (L391-L419)
  - [Container logs by pod labels (e.g. skaffold)](#container-logs-for-a-pod-with-a-specific-label) (L420-L447)
  - [Container logs filtered by textPayload/jsonPayload](#container-error-logs-for-a-specific-pod-containing-a-post-in-the-textpayload) (L448-L467)
  - [Container errors in kube-system & insights](#container-errors-logs-in-the-kube-system-namespace) (L468-L484)
  - [Kubernetes container logs](#kubernetes-container-logs) (L485-L492)
  - [TPU node container logs](#stdout-container-logs-across-all-tpu-nodes-with-the-same-prefix) (L523-L541)
  - [GKE Job / JobSet logs](#stdout-container-logs-from-the-same-gke-job) (L542-L579)
- [Cluster Administration & Control Plane](#google-kubernetes-engine-cluster-operations) (L79-L104, L114-L131, L140-L166, L176-L208, L493-L522, L580-L611)
  - [GKE cluster operations](#google-kubernetes-engine-cluster-operations) (L79-L86)
  - [GKE cluster creation](#google-kubernetes-engine-cluster-creation) (L87-L95)
  - [Kubernetes cluster deployment](#kubernetes-cluster-deployment) (L96-L104)
  - [Kubernetes cluster operations and events (us-central1-b)](#kubernetes-cluster-operations-and-events-in-us-central1-b) (L114-L121)
  - [Pod requests by user](#kubernetes-pod-requests-from-users) (L122-L131)
  - [Endpoints update](#kubernetes-endpoints-update) (L140-L148)
  - [Control plane logs (k8s.io & container.googleapis.com)](#kubernetes-control-plane-logs) (L149-L166)
  - [Pod & Node audit logs from control plane](#kubernetes-pod-audit-logs-from-control-plane) (L176-L208)
  - [Addon Manager & control plane errors](#kubernetes-cluster-control-plane-for-addon-manager-activity) (L209-L231)
  - [Control plane component logs (apiserver, scheduler, controller-manager)](#kubernetes-api-server-logs) (L493-L522)
  - [Node auto-repair & cluster deletion](#node-auto-repair-events) (L580-L598)
  - [Pod IP assignment and release](#pod-ip-assignment-and-release) (L599-L611)
- [Autoscaling & Controllers](#ingress-controller-events) (L232-L264, L274-L296)
  - [Ingress Controller events](#ingress-controller-events) (L232-L242)
  - [Service Controller events (kube-controller-manager)](#service-controller-events-kube-controller-manager) (L243-L253)
  - [Cluster Autoscaler events](#cluster-autoscaler-events) (L254-L264)
  - [Scheduler events (including preemptions)](#scheduler-events) (L274-L296)
- [Node Status & System logs](#node-events) (L297-L373)
  - [Node events](#node-events) (L297-L304)
  - [Out of memory (OOM) events](#out-of-memory-oom-events) (L305-L314)
  - [Kube-proxy logs](#looking-at-kube-proxy-logs) (L315-L322)
  - [Dockerd logs](#looking-at-dockerd-logs) (L323-L330)
  - [Kubelet errors or failures](#looking-at-kubelet-errors-or-failures) (L331-L339)
  - [Node logs for GKE system logs](#looking-at-node-logs-for-gke-system-logs) (L340-L356)
  - [Container & pod logs for GKE system logs](#container-and-pod-logs-for-gke-system-logs) (L357-L373)
- [Security & Authentication](#kubernetes-cluster-authentication-failure) (L105-L113)

---

## Cluster logs in a specific location
Finds cluster logs for a specific Google Cloud location.
**Variables to replace:** `<LOCATION>`

```lql
resource.type="k8s_cluster" AND
resource.labels.location="<LOCATION>"
```

## Pod eviction events
Finds Kubernetes events where a pod was evicted.
**Variables to replace:** None

```lql
resource.type="k8s_pod" AND
log_id("events") AND
jsonPayload.reason="Evicted"
```

## Container errors
Finds errors from a specific pod.
**Variables to replace:** `<POD_NAME>`

```lql
resource.type="k8s_container" AND
resource.labels.pod_name="<POD_NAME>" AND
severity=ERROR
```

## Google Kubernetes Engine cluster operations
**Variables to replace:** None

```lql
resource.type="gke_cluster" AND
log_id("cloudaudit.googleapis.com/activity")
```

## Google Kubernetes Engine cluster creation
**Variables to replace:** None

```lql
resource.type="gke_cluster" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.methodName="google.container.v1.ClusterManager.CreateCluster"
```

## Kubernetes cluster deployment
**Variables to replace:** None

```lql
resource.type="k8s_cluster" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.methodName:"deployments"
```

## Kubernetes cluster authentication failure
**Variables to replace:** None

```lql
resource.type="k8s_cluster" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.authenticationInfo.principalEmail="system:anonymous"
```

## Kubernetes cluster operations and events in us-central1-b
**Variables to replace:** None

```lql
resource.type="k8s_cluster" AND
resource.labels.location="us-central1-b"
```

## Kubernetes pod requests from users
**Variables to replace:** `<USER_EMAIL>`

```lql
resource.type="k8s_cluster" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.methodName:"io.k8s.core.v1.pods" AND
protoPayload.authenticationInfo.principalEmail="<USER_EMAIL>"
```

## Kubernetes events
**Variables to replace:** None

```lql
resource.type="k8s_cluster" AND
log_id("events")
```

## Kubernetes endpoints update
**Variables to replace:** None

```lql
resource.type="k8s_cluster" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.request.kind="Endpoints"
```

## Kubernetes control plane logs
**Variables to replace:** None

```lql
resource.type="k8s_cluster" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.serviceName="k8s.io"
```

## Kubernetes Engine control plane logs
**Variables to replace:** None

```lql
resource.type="k8s_cluster" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.serviceName="container.googleapis.com"
```

## Pod deletion
**Variables to replace:** None

```lql
resource.type="k8s_cluster" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.methodName=~"io\.k8s\.core\.v1\.pods\.(create|delete)"
```

## Kubernetes pod audit logs from control plane
**Variables to replace:** `<CLUSTER_LOCATION>`, `<CLUSTER_NAME>`, `<POD_NAME>`, `<POD_NAMESPACE>`

```lql
resource.type="k8s_cluster" AND
resource.labels.location="<CLUSTER_LOCATION>" AND
resource.labels.cluster_name="<CLUSTER_NAME>" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.resourceName="core/v1/namespaces/<POD_NAMESPACE>/pods/<POD_NAME>"
```

## Kubernetes pod evictions
**Variables to replace:** `<CLUSTER_LOCATION>`, `<CLUSTER_NAME>`

```lql
resource.type="k8s_cluster" AND
resource.labels.location="<CLUSTER_LOCATION>" AND
resource.labels.cluster_name="<CLUSTER_NAME>" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.methodName="io.k8s.core.v1.pods.eviction.create"
```

## Kubernetes node audit logs from the control plane
**Variables to replace:** `<CLUSTER_LOCATION>`, `<CLUSTER_NAME>`

```lql
resource.type="k8s_cluster" AND
resource.labels.location="<CLUSTER_LOCATION>" AND
resource.labels.cluster_name="<CLUSTER_NAME>" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.methodName:"io.k8s.core.v1.nodes"
```

## Kubernetes cluster control plane for Addon Manager Activity
**Variables to replace:** `<CLUSTER_LOCATION>`, `<CLUSTER_NAME>`

```lql
resource.type="k8s_cluster" AND
resource.labels.location="<CLUSTER_LOCATION>" AND
resource.labels.cluster_name="<CLUSTER_NAME>" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.authenticationInfo.principalEmail="system:addon-manager"
```

## Kubernetes control plane errors (excluding Conflict , which is normal)
**Variables to replace:** `<CLUSTER_LOCATION>`, `<CLUSTER_NAME>`

```lql
resource.type="k8s_cluster" AND
resource.labels.location="<CLUSTER_LOCATION>" AND
resource.labels.cluster_name="<CLUSTER_NAME>" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.status.message!="Conflict" AND
protoPayload.status.code!=0
```

## Ingress Controller events
**Variables to replace:** `<CLUSTER_LOCATION>`, `<CLUSTER_NAME>`

```lql
resource.type="k8s_cluster" AND
resource.labels.location="<CLUSTER_LOCATION>" AND
resource.labels.cluster_name="<CLUSTER_NAME>" AND
log_id("events") AND
jsonPayload.source.component="loadbalancer-controller"
```

## Service Controller events (kube-controller-manager)
**Variables to replace:** `<CLUSTER_LOCATION>`, `<CLUSTER_NAME>`

```lql
resource.type="k8s_cluster" AND
resource.labels.location="<CLUSTER_LOCATION>" AND
resource.labels.cluster_name="<CLUSTER_NAME>" AND
log_id("events") AND
jsonPayload.source.component="service-controller"
```

## Cluster Autoscaler events
**Variables to replace:** `<CLUSTER_LOCATION>`, `<CLUSTER_NAME>`

```lql
resource.type="k8s_cluster" AND
resource.labels.location="<CLUSTER_LOCATION>" AND
resource.labels.cluster_name="<CLUSTER_NAME>" AND
log_id("events") AND
jsonPayload.source.component="cluster-autoscaler"
```

## Query pod during creation
**Variables to replace:** `<POD_NAME>`

```lql
resource.type="k8s_pod" AND
resource.labels.pod_name="<POD_NAME>" AND
log_id("events")
```

## Scheduler events
**Variables to replace:** `<CLUSTER_LOCATION>`, `<CLUSTER_NAME>`

```lql
resource.type="k8s_pod" AND
resource.labels.location="<CLUSTER_LOCATION>" AND
resource.labels.cluster_name="<CLUSTER_NAME>" AND
log_id("events") AND
jsonPayload.source.component="default-scheduler"
```

## Scheduler events (preemptions)
**Variables to replace:** `<CLUSTER_LOCATION>`, `<CLUSTER_NAME>`

```lql
resource.type="k8s_pod" AND
resource.labels.location="<CLUSTER_LOCATION>" AND
resource.labels.cluster_name="<CLUSTER_NAME>" AND
log_id("events") AND
jsonPayload.source.component="default-scheduler" AND
jsonPayload.reason="Preempted"
```

## Node events
**Variables to replace:** None

```lql
resource.type="k8s_node" AND
log_id("events")
```

## Out of memory (OOM) events
**Variables to replace:** None

```lql
resource.type="k8s_node"
log_id("events")
(jsonPayload.reason:("OOMKilling" OR "SystemOOM")
  OR jsonPayload.message:("OOM encountered" OR "out of memory"))
```

## Looking at Kube-proxy logs
**Variables to replace:** None

```lql
resource.type="k8s_node" AND
log_id("kube-proxy")
```

## Looking at dockerd logs
**Variables to replace:** None

```lql
resource.type="k8s_node" AND
log_id("container-runtime")
```

## Looking at kubelet errors or failures
**Variables to replace:** None

```lql
resource.type="k8s_node" AND
log_id("kubelet") AND
jsonPayload.MESSAGE:("error" OR "fail")
```

## Looking at node logs for GKE system logs
**Variables to replace:** None

```lql
resource.type = "k8s_node" AND
logName:( "logs/container-runtime" OR
"logs/docker" OR
"logs/kube-container-runtime-monitor" OR
"logs/kube-logrotate" OR
"logs/kube-node-configuration" OR
"logs/kube-node-installation" OR
"logs/kubelet" OR
"logs/kubelet-monitor" OR
"logs/node-journal" OR
"logs/node-problem-detector")
```

## Container and pod logs for GKE system logs
**Variables to replace:** None

```lql
resource.type = ("k8s_container" OR "k8s_pod") AND
resource.labels.namespace_name = (
"cnrm-system" OR
"config-management-system" OR
"gatekeeper-system" OR
"gke-connect" OR
"gke-system" OR
"istio-system" OR
"knative-serving" OR
"monitoring-system" OR
"kube-system")
```

## Stdout container logs across all pods and containers in a cluster
**Variables to replace:** None

```lql
resource.type="k8s_container" AND
log_id("stdout")
```

## Container error logs across all pods and containers in a cluster
**Variables to replace:** None

```lql
resource.type="k8s_container" AND
log_id("stderr") AND
severity=ERROR
```

## Container error logs for a pod with a specific name
**Variables to replace:** `<POD_NAME>`

```lql
resource.type="k8s_container" AND
resource.labels.pod_name="<POD_NAME>" AND
severity=ERROR
```

## Container error logs for a specific container in a specific pod
**Variables to replace:** `<POD_NAME>`

```lql
resource.type="k8s_container" AND
resource.labels.pod_name="<POD_NAME>" AND
resource.labels.container_name="server" AND
severity=ERROR
```

## Container error logs for a specific namespace and container
**Variables to replace:** None

```lql
resource.type="k8s_container" AND
resource.labels.namespace_name="istio-system" AND
resource.labels.container_name="egressgateway" AND
severity=ERROR
```

## Container logs for a pod with a specific label
**Variables to replace:** None

```lql
resource.type="k8s_container" AND
labels."k8s-pod/app"="loadgenerator" AND
severity=ERROR
```

## Container error logs for pods running on a specific node
**Variables to replace:** `<NODE_NAME>`

```lql
resource.type="k8s_container" AND
labels."compute.googleapis.com/resource_name"="<NODE_NAME>" AND
severity=ERROR
```

## Container logs for a pod with a label generated using skaffold
**Variables to replace:** `<SKAFFOLD_RUN_ID>`

```lql
resource.type="k8s_container" AND
labels."k8s-pod/app"="loadgenerator" AND
labels."k8s-pod/skaffold_dev/run-id"="<SKAFFOLD_RUN_ID>" AND
severity=ERROR
```

## Container error logs for a specific pod containing a POST in the textPayload
**Variables to replace:** `<POD_NAME>`

```lql
resource.type="k8s_container" AND
resource.labels.pod_name="<POD_NAME>" AND
textPayload:"POST" AND
severity=ERROR
```

## Container error logs for a specific pod containing a GET in the structured JSON
**Variables to replace:** `<POD_NAME>`

```lql
resource.type="k8s_container" AND
resource.labels.pod_name="<POD_NAME>" AND
jsonPayload."http.req.method"="GET" AND
severity=ERROR
```

## Container errors logs in the kube-system namespace
**Variables to replace:** None

```lql
resource.type="k8s_container" AND
resource.labels.namespace_name="kube-system" AND
severity=ERROR
```

## Container error in the container insights log
**Variables to replace:** None

```lql
resource.type="k8s_container" AND
log_id("clouderrorreporting.googleapis.com/insights")
```

## Kubernetes container logs
**Variables to replace:** `<CONTAINER_NAME>`

```lql
resource.type="k8s_container" AND
resource.labels.container_name="<CONTAINER_NAME>"
```

## Kubernetes API server logs
**Variables to replace:** `<CLUSTER_LOCATION>`, `<CLUSTER_NAME>`

```lql
resource.type="k8s_control_plane_component" AND
resource.labels.component_name="apiserver" AND
resource.labels.location="<CLUSTER_LOCATION>" AND
resource.labels.cluster_name="<CLUSTER_NAME>"
```

## Kubernetes Scheduler logs
**Variables to replace:** `<CLUSTER_LOCATION>`, `<CLUSTER_NAME>`

```lql
resource.type="k8s_control_plane_component" AND
resource.labels.component_name="scheduler" AND
resource.labels.location="<CLUSTER_LOCATION>" AND
resource.labels.cluster_name="<CLUSTER_NAME>"
```

## Kubernetes Controller Manager logs
**Variables to replace:** `<CLUSTER_LOCATION>`, `<CLUSTER_NAME>`

```lql
resource.type="k8s_control_plane_component" AND
resource.labels.component_name="controller-manager" AND
resource.labels.location="<CLUSTER_LOCATION>" AND
resource.labels.cluster_name="<CLUSTER_NAME>"
```

## Stdout container logs across all TPU nodes with the same prefix
**Variables to replace:** `<TPU_NODE_PREFIX>`

```lql
resource.type="k8s_container" AND
labels."compute.googleapis.com/resource_name"=~"<TPU_NODE_PREFIX>.*" AND
log_id("stdout")
```

## Container error logs across all TPU nodes with the same prefix
**Variables to replace:** `<TPU_NODE_PREFIX>`

```lql
resource.type="k8s_container" AND
labels."compute.googleapis.com/resource_name"=~"<TPU_NODE_PREFIX>.*" AND
log_id("stderr") AND
severity=ERROR
```

## Stdout container logs from the same GKE Job
**Variables to replace:** `<JOB_NAME>`

```lql
resource.type="k8s_container" AND
labels."k8s-pod/batch.kubernetes.io/job-name" = "<JOB_NAME>" AND
log_id("stdout")
```

## Container error logs from the same GKE Job
**Variables to replace:** `<JOB_NAME>`

```lql
resource.type="k8s_container" AND
labels."k8s-pod/batch.kubernetes.io/job-name"="<JOB_NAME>" AND
log_id("stderr") AND
severity=ERROR
```

## Stdout container logs from the same GKE JobSet
**Variables to replace:** `<JOBSET_NAME>`

```lql
resource.type="k8s_container" AND
labels."k8s-pod/jobset_sigs_k8s_io/jobset-name"="<JOBSET_NAME>" AND
log_id("stdout")
```

## Container error logs from the same GKE JobSet
**Variables to replace:** `<JOBSET_NAME>`

```lql
resource.type="k8s_container" AND
labels."k8s-pod/jobset_sigs_k8s_io/jobset-name"="<JOBSET_NAME>" AND
log_id("stderr") AND
severity=ERROR
```

## Node auto-repair events
**Variables to replace:** `<CLUSTER_NAME>`

```lql
resource.type="gke_nodepool" AND
resource.labels.cluster_name="<CLUSTER_NAME>" AND
log_id("cloudaudit.googleapis.com/activity") AND
protoPayload.methodName="google.container.v1.ClusterManager.RepairNodePool"
```

## Cluster deletion events
**Variables to replace:** `<CLUSTER_NAME>`

```lql
resource.type="gke_cluster" AND
resource.labels.cluster_name="<CLUSTER_NAME>" AND
protoPayload.methodName:"DeleteCluster"
```

## Pod IP assignment and release
**Variables to replace:** `<CLUSTER_NAME>`, `<POD_NAME>`

```lql
resource.type="k8s_cluster" AND
resource.labels.cluster_name="<CLUSTER_NAME>" AND
protoPayload.resourceName:"<POD_NAME>" AND
((protoPayload.methodName="io.k8s.core.v1.pods.status.patch" AND
  protoPayload.request.status.podIP:*) OR
 (protoPayload.methodName="io.k8s.core.v1.pods.delete" AND
  protoPayload.response.status.podIP:*))
```
