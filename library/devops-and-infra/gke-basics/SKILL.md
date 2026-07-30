---
name: gke-basics
description: ">- Core GKE cluster discovery and hub. Use to route to specialized GKE skills. Do not use for specialized tasks (networking, security, etc.) directly."
category: devops-and-infra
source_repo: google/skills
source_path: "skills/cloud/gke-basics/SKILL.md"
source_url: https://github.com/google/skills/blob/HEAD/skills/cloud/gke-basics/SKILL.md
---


# GKE Basics

Managed Kubernetes platform on Google Cloud. Defaults to Autopilot mode.

## Quick Start

```bash
gcloud services enable container.googleapis.com --quiet
gcloud container clusters create-auto my-cluster --region=us-central1 --quiet
gcloud container clusters get-credentials my-cluster --region=us-central1 --quiet
```

## GKE Skill Routing Table

Load the single, most specific GKE sub-skill below matching your workload
requirements. **Do not load multiple GKE skills unless explicitly required.**

| Scenario             | Trigger Keywords        | Target Skill                |
| -------------------- | ----------------------- | --------------------------- |
| Golden Path Defaults | production defaults,    | `gke-golden-path`           |
:                      : golden path             :                             :
| Cluster Creation     | create cluster,         | `gke-cluster-creation`      |
:                      : provision GKE           :                             :
| Networking & Ingress | private cluster, VPC,   | `gke-networking`,           |
:                      : Gateway API, Ingress,   : `gke-service-networking`    :
:                      : DNS                     :                             :
| Security & IAM       | Workload Identity,      | `gke-platform-security`,    |
:                      : Secret Manager, RBAC,   : `gke-workload-security`     :
:                      : hardening               :                             :
| Autoscaling          | HPA, VPA, Cluster       | `gke-workload-scaling`      |
:                      : Autoscaler, NAP         :                             :
| Compute Classes      | ComputeClass, Spot      | `gke-compute-classes`       |
:                      : fallback, GPU/TPU nodes :                             :
| Cost Analysis        | BigQuery billing        | `gke-cost-analysis`         |
:                      : exports, budgets, live  :                             :
:                      : monitoring              :                             :
| Cost Optimization    | Spot VMs, rightsizing,  | `gke-cost-optimization`     |
:                      : quotas                  :                             :
| AI/ML Workloads      | LLM, GPU/TPU inference, | `gke-inference`             |
:                      : serving, vLLM           :                             :
| GPU/TPU Disruption   | GPU termination, TPU    | `gke-ai-troubleshooting-`   |
:                      : shutdown, host          : `handle-disruption-gpu-tpu` :
:                      : maintenance             :                             :
| Cluster Upgrades     | upgrade, maintenance    | `gke-upgrades`              |
:                      : window, release channel :                             :
| Observability        | monitoring, logging,    | `gke-observability`         |
:                      : Prometheus, dashboards  :                             :
| Multi-tenancy        | namespace isolation,    | `gke-multitenancy`          |
:                      : resource quota,         :                             :
:                      : LimitRange              :                             :
| Batch & HPC          | batch, HPC, Kueue,      | `gke-batch-hpc`             |
:                      : JobSet, parallel jobs   :                             :
| App Onboarding       | containerize,           | `gke-app-onboarding`        |
:                      : Dockerfile, deploy app, :                             :
:                      : onboard                 :                             :
| Backup & DR          | backup plan, restore,   | `gke-backup-dr`             |
:                      : disaster recovery, CMEK :                             :
| Storage & PVC        | SSD, PV, PVC,           | `gke-storage`               |
:                      : StorageClass, GCS FUSE  :                             :
| Reliability          | PDB, health probe,      | `gke-reliability`           |
:                      : liveness, readiness     :                             :
| Productionization    | production readiness,   | `gke-productionize`         |
:                      : productionize,          :                             :
:                      : readiness scoring,      :                             :
:                      : audit cluster           :                             :

## Conceptual & Informational Queries (CRITICAL)

For purely conceptual, educational, or informational questions (e.g. "What is
GKE?", "Explain GKE architecture", or "Compare Standard vs Autopilot" in a
generic sense):

*   **Rule**: **Answer immediately using your pre-trained knowledge.**
*   **Constraint**: **Do not execute code searches, directory listings, or other
    tool calls** unless the user explicitly requests you to inspect the local
    workspace or run a command. Keep it fast, cheap, and direct.

---

**Source:** [`google/skills`](https://github.com/google/skills) → `skills/cloud/gke-basics/SKILL.md`
