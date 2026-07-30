# Networking LQL Queries

## Table of Contents

- [Firewall rules logs](#firewall-all-logs) (L28-L70)
  - [Firewall - all logs](#firewall-all-logs) (L28-L35)
  - [Firewall logs for a given country](#firewall-logs-for-a-given-country) (L36-L44)
  - [Firewall logs from a VM](#firewall-logs-from-a-vm) (L45-L53)
  - [Firewall subnet logs](#firewall-subnet-logs) (L54-L62)
  - [Compute Engine subnetwork traffic logs](#compute-engine-subnetwork-traffic-logs-to-a-subnet) (L63-L70)
- [VPC and VPN logs](#vpc-flow-logs) (L71-L123, L149-L167)
  - [VPC flow logs - overview](#vpc-flow-logs) (L71-L78)
  - [VPC flow logs by port/protocol](#vpc-flow-logs-for-specific-port-and-protocol) (L79-L88)
  - [VPC flow logs by subnet](#vpc-flow-logs-for-specific-subnet) (L89-L97)
  - [VPC flow logs by subnet prefix](#vpc-flow-logs-for-specific-subnet-prefix) (L98-L106)
  - [VPC flow logs by VM](#vpc-flow-logs-for-a-specific-vm) (L107-L115)
  - [VPN gateway logs](#vpn-gateway-logs) (L116-L123)
  - [VPN gateway peer not responding](#vpn-gateway-peer-not-responding) (L149-L156)
  - [VPC flow logs egress](#vpc-flow-logs-egress-excluding-internal-traffic) (L157-L167)
- [Gateways and Load Balancers](#http-load-balancer-5xx-errors) (L124-L148, L168-L177)
  - [HTTP load balancer 5xx errors](#http-load-balancer-5xx-errors) (L124-L131)
  - [HTTP load balancer PHPMyAdmin requests](#http-load-balancer-requests-to-phpmyadmin) (L132-L139)
  - [HTTP load balancer spillover events](#http-load-balancer-spillover-events) (L140-L148)
  - [Cloud CDN signed URL 403 errors](#cloud-cdn-signed-url-403-errors) (L168-L177)

---

## Firewall - all logs {#firewall-all-logs}
**Variables to replace:** None

```lql
resource.type="gce_subnetwork" AND
log_id("compute.googleapis.com/firewall")
```

## Firewall logs for a given country
**Variables to replace:** `<COUNTRY_ISO_ALPHA_3>`

```lql
resource.type="gce_subnetwork" AND
log_id("compute.googleapis.com/firewall") AND
jsonPayload.remote_location.country="<COUNTRY_ISO_ALPHA_3>"
```

## Firewall logs from a VM
**Variables to replace:** `<INSTANCE_NAME>`

```lql
resource.type="gce_subnetwork" AND
log_id("compute.googleapis.com/firewall") AND
jsonPayload.instance.vm_name="<INSTANCE_NAME>"
```

## Firewall subnet logs
**Variables to replace:** `<SUBNET_NAME>`

```lql
resource.type="gce_subnetwork" AND
log_id("compute.googleapis.com/firewall") AND
resource.labels.subnetwork_name="<SUBNET_NAME>"
```

## Compute Engine subnetwork traffic logs to a subnet
**Variables to replace:** `<SUBNET_IP>`

```lql
resource.type="gce_subnetwork" AND
ip_in_net(jsonPayload.connection.dest_ip, "<SUBNET_IP>")
```

## VPC flow logs
**Variables to replace:** None

```lql
resource.type="gce_subnetwork" AND
log_id("compute.googleapis.com/vpc_flows")
```

## VPC flow logs for specific port and protocol
**Variables to replace:** `<PORT_ID>`, `<PROTOCOL>`

```lql
resource.type="gce_subnetwork" AND
log_id("compute.googleapis.com/vpc_flows") AND
jsonPayload.connection.src_port="<PORT_ID>" AND
jsonPayload.connection.protocol="<PROTOCOL>"
```

## VPC flow logs for specific subnet
**Variables to replace:** `<SUBNET_NAME>`

```lql
resource.type="gce_subnetwork" AND
log_id("compute.googleapis.com/vpc_flows") AND
resource.labels.subnetwork_name="<SUBNET_NAME>"
```

## VPC flow logs for specific subnet prefix
**Variables to replace:** `<SUBNET_IP>`

```lql
resource.type="gce_subnetwork" AND
log_id("compute.googleapis.com/vpc_flows") AND
ip_in_net(jsonPayload.connection.dest_ip, "<SUBNET_IP>")
```

## VPC flow logs for a specific VM
**Variables to replace:** `<VM_NAME>`

```lql
resource.type="gce_subnetwork" AND
log_id("compute.googleapis.com/vpc_flows") AND
jsonPayload.src_instance.vm_name="<VM_NAME>"
```

## VPN gateway logs
**Variables to replace:** `<GATEWAY_ID>`

```lql
resource.type="vpn_gateway" AND
resource.labels.gateway_id="<GATEWAY_ID>"
```

## HTTP load balancer 5xx errors
**Variables to replace:** None

```lql
resource.type="http_load_balancer" AND
httpRequest.status>=500
```

## HTTP load balancer requests to PHPMyAdmin
**Variables to replace:** None

```lql
resource.type="http_load_balancer" AND
httpRequest.request_url:"phpmyadmin"
```

## HTTP load balancer spillover events
**Variables to replace:** `<BACKEND_SERVICE_NAME>`

```lql
resource.type="http_load_balancer" AND
resource.labels.backend_service_name="<BACKEND_SERVICE_NAME>" AND
jsonPayload.statusDetails=~"(spilled_over|overflow|spillover)"
```

## VPN gateway peer not responding
**Variables to replace:** None

```lql
resource.type="vpn_gateway"
"establishing IKE_SA failed, peer not responding"
```

## VPC flow logs egress (excluding internal traffic)
**Variables to replace:** `<VPC_NAME>`

```lql
resource.type="gce_subnetwork" AND
logName=~"vpc_flows" AND
jsonPayload.reporter="SRC" AND
jsonPayload.src_vpc.vpc_name="<VPC_NAME>" AND
(jsonPayload.dest_vpc.vpc_name!="<VPC_NAME>" OR NOT jsonPayload.dest_vpc:*)
```

## Cloud CDN signed URL 403 errors
**Variables to replace:** `<FORWARDING_RULE_NAME>`, `<REQUEST_URL>`

```lql
resource.type="http_load_balancer" AND
resource.labels.forwarding_rule_name="<FORWARDING_RULE_NAME>" AND
httpRequest.requestUrl="<REQUEST_URL>" AND
jsonPayload.statusDetails="signed_request_key_not_found"
```
