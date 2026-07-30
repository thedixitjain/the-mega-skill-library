# Third-party application LQL Queries


## Apache logs
**Variables to replace:** None

```lql
resource.type="gce_instance" AND
(logName:"/apache-access" OR logName:"/apache-error")
```

## Cassandra logs
**Variables to replace:** None

```lql
resource.type="gce_instance" AND
log_id("cassandra")
```

## Chef logs
**Variables to replace:** `<PROJECT_ID>`

```lql
resource.type="gce_instance" AND
logName:"projects/<PROJECT_ID>/logs/chef-"
```

## Gitlab logs
**Variables to replace:** `<PROJECT_ID>`

```lql
resource.type="gce_instance" AND
logName:"projects/<PROJECT_ID>/logs/gitlab-"
```

## Jenkins logs
**Variables to replace:** None

```lql
resource.type="gce_instance" AND
log_id("jenkins")
```

## Jetty logs
**Variables to replace:** `<PROJECT_ID>`

```lql
resource.type="gce_instance" AND
logName:"projects/<PROJECT_ID>/logs/jetty-"
```

## Joomla logs
**Variables to replace:** None

```lql
resource.type="gce_instance" AND
log_id("joomla")
```

## Linux syslogs
**Variables to replace:** None

```lql
resource.type="gce_instance" AND
log_id("syslog")
```

## Magneto logs
**Variables to replace:** `<PROJECT_ID>`

```lql
resource.type="gce_instance" AND
logName:"projects/<PROJECT_ID>/logs/magneto-"
```

## Mediawiki logs
**Variables to replace:** None

```lql
resource.type="gce_instance" AND
log_id("mediawiki")
```

## memcached logs
**Variables to replace:** None

```lql
resource.type="gce_instance" AND
log_id("memcached")
```

## MongoDB logs
**Variables to replace:** None

```lql
resource.type="gce_instance" AND
log_id("mongodb")
```

## MySQL logs
**Variables to replace:** None

```lql
resource.type="gce_instance" AND
log_id("mysql")
```

## Nginx logs
**Variables to replace:** `<PROJECT_ID>`

```lql
resource.type="gce_instance" AND
logName:"projects/<PROJECT_ID>/logs/nginx-"
```

## PostgreSQL logs
**Variables to replace:** None

```lql
resource.type="gce_instance" AND
log_id("postgresql")
```

## Puppet logs
**Variables to replace:** `<PROJECT_ID>`

```lql
resource.type="gce_instance" AND
logName:"projects/<PROJECT_ID>/logs/puppet-"
```

## RabbitMQ logs
**Variables to replace:** `<PROJECT_ID>`

```lql
resource.type="gce_instance" AND
logName:"projects/<PROJECT_ID>/logs/rabbitmq-"
```

## Redmine logs
**Variables to replace:** None

```lql
resource.type="gce_instance" AND
log_id("redmine")
```

## Salt logs
**Variables to replace:** `<PROJECT_ID>`

```lql
resource.type="gce_instance" AND
logName:"projects/<PROJECT_ID>/logs/salt-"
```

## Slow MySQL queries
**Variables to replace:** None

```lql
resource.type="gce_instance" AND
log_id("mysql-slow")
```

## Solr logs
**Variables to replace:** None

```lql
resource.type="gce_instance" AND
log_id("solr")
```

## SugarCRM logs
**Variables to replace:** None

```lql
resource.type="gce_instance" AND
log_id("sugarcrm")
```

## Tomcat logs
**Variables to replace:** None

```lql
resource.type="gce_instance" AND
log_id("tomcat")
```

## Zookeeper logs
**Variables to replace:** None

```lql
resource.type="gce_instance" AND
log_id("zookeeper")
```
