# Cloud SQL LQL Queries


## Cloud SQL audit logs
**Variables to replace:** `<DATABASE_ID>`

```lql
resource.type="cloudsql_database" AND
resource.labels.database_id="<DATABASE_ID>" AND
log_id("cloudaudit.googleapis.com/activity")
```

## Cloud SQL MySQL error logs
**Variables to replace:** None

```lql
resource.type="cloudsql_database" AND
log_id("cloudsql.googleapis.com/mysql.err")
```

## Cloud SQL MySQL-based databases
**Variables to replace:** `<DATABASE_ID>`

```lql
resource.type="cloudsql_database" AND
resource.labels.database_id="<DATABASE_ID>" AND
log_id("cloudsql.googleapis.com/mysql")
```

## Cloud SQL Postgres-based databases
**Variables to replace:** `<DATABASE_ID>`

```lql
resource.type="cloudsql_database" AND
resource.labels.database_id="<DATABASE_ID>" AND
log_id("cloudsql.googleapis.com/postgres.log")
```

## Cloud SQL SQL Server error logs
**Variables to replace:** None

```lql
resource.type="cloudsql_database" AND
log_id("cloudsql.googleapis.com/sqlserver.err")
```

## Cloud SQL SQL Server-based databases
**Variables to replace:** `<DATABASE_ID>`

```lql
resource.type="cloudsql_database" AND
resource.labels.database_id="<DATABASE_ID>" AND
log_id("cloudsql.googleapis.com/sqlagent.out")
```
