# Integration with Other Tools

## With Vite

Vite uses port 5173 for dev, 4173 for preview:

```json
{
  "portMonitor.hosts": {
    "Vite": {
      "5173": "dev",
      "4173": "preview"
    }
  }
}
```

## With Next.js

Next.js typically uses port 3000:

```json
{
  "portMonitor.hosts": {
    "Next.js": {
      "3000": "app"
    }
  }
}
```

## With Docker Compose

Monitor exposed ports from docker-compose.yml:

```json
{
  "portMonitor.hosts": {
    "Docker": {
      "8080": "web",
      "5432": "postgres",
      "6379": "redis"
    }
  }
}
```

## With Microservices

Monitor multiple services across different ports:

```json
{
  "portMonitor.hosts": {
    "Frontend": {
      "3000": "web",
      "3001": "admin"
    },
    "Backend": {
      "8080": "api",
      "8081": "auth"
    },
    "Database": {
      "5432": "postgres",
      "6379": "redis",
      "27017": "mongo"
    }
  }
}
```
