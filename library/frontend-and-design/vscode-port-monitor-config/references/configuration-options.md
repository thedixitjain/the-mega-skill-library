# Configuration Options Reference

## portMonitor.hosts

Main configuration object for monitored ports.

**Format**:
```json
{
  "GroupName": {
    "port": "label",
    "__CONFIG": { ... }
  }
}
```

**Supported formats**:
- Simple array: `["3000", "3001"]`
- Port range: `["3000-3009"]`
- Object with labels: `{"3000": "dev", "3001": "api"}`
- Well-known ports: `["http", "https", "postgresql"]`

## __CONFIG Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `compact` | boolean | false | Compact display mode |
| `bgcolor` | string | none | Background color |
| `show_title` | boolean | false | Show group title |
| `separator` | string | "\\|" | Port separator |

**Background colors**:
- Simple: `"red"`, `"yellow"`, `"blue"`, `"green"`
- VS Code theme: `"statusBarItem.errorBackground"`, `"statusBarItem.warningBackground"`

## portMonitor.statusIcons

Customize status icons.

```json
{
  "inUse": "🟢 ",
  "free": "⚪️ "
}
```

**Tip**: Add space after emoji for better readability: `"🟢 "` instead of `"🟢"`

## portMonitor.intervalMs

Monitoring refresh interval in milliseconds.

- **Default**: 3000 (3 seconds)
- **Minimum**: 1000 (1 second)
- **Recommended**: 3000-5000 for balance between responsiveness and performance

## portMonitor.statusBarPosition

Status bar display position.

- `"left"` - Left side of status bar
- `"right"` - Right side of status bar (default)

## portMonitor.enableProcessKill

Enable process termination feature.

- `true` - Allow killing processes via status bar (default)
- `false` - Disable process management

## portMonitor.displayOptions.showFullPortNumber

Show full port numbers in display.

- `true` - Show complete port numbers
- `false` - May abbreviate in compact mode
