# Advanced Configuration

## Pattern Match Labels

Use wildcards for dynamic labeling:

```json
{
  "portMonitor.portLabels": {
    "3000": "main-app",
    "300*": "dev-env",
    "8080": "proxy",
    "*": "service"
  }
}
```

## Custom Port Emojis

```json
{
  "portMonitor.portEmojis": {
    "dev": "🚀",
    "api": "⚡",
    "db": "🗄️"
  }
}
```

## Multiple Separators

```json
{
  "__CONFIG": {
    "separator": " → "
  }
}
```

**Display**: `Project: [🟢 dev:5173 → ⚪️ preview:4173]`

## Quick Reference

### Common Ports

| Port | Service | Label Suggestion |
|------|---------|------------------|
| 3000 | Next.js / React | `"app"` or `"dev"` |
| 5173 | Vite | `"dev"` |
| 4173 | Vite Preview | `"preview"` |
| 8080 | Generic HTTP | `"web"` |
| 5432 | PostgreSQL | `"postgres"` |
| 6379 | Redis | `"redis"` |
| 27017 | MongoDB | `"mongo"` |
| 3306 | MySQL | `"mysql"` |

### Keyboard Shortcuts

- Click port in status bar → Show port details
- Right-click port → Kill process using port
- `Cmd+Shift+P` → "Port Monitor: Refresh" → Force refresh status
