# Cloud Source Repositories LQL Queries


## Cloud Source Repository logs
**Variables to replace:** `<REPOSITORY_NAME>`

```lql
resource.type="csr_repository" AND
resource.labels.name="<REPOSITORY_NAME>"
```
