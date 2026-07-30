# Troubleshooting Guide

## Issue 1: Port Monitor Not Showing

**Symptoms**: Status bar doesn't show port status

**Solutions**:
1. Check if extension is installed:
   ```bash
   code --list-extensions | grep port-monitor
   ```

2. Verify configuration in `.vscode/settings.json`

3. Reload VS Code window: `Cmd+Shift+P` → "Reload Window"

## Issue 2: Configuration Errors

**Symptoms**: "Port Monitor: Configuration Error" in status bar

**Common causes**:
- Reversed port-label format
- Empty host name
- Invalid JSON syntax

**Fix**: Check configuration format:
```json
// ❌ Wrong
{
  "localhost": {
    "dev": 5173  // Reversed!
  }
}

// ✅ Correct
{
  "localhost": {
    "5173": "dev"
  }
}
```

## Issue 3: Ports Not Detected

**Symptoms**: All ports show as ⚪️ (free) when they're actually in use

**Solutions**:
1. Check if ports are actually in use:
   ```bash
   lsof -i :5173
   ```

2. Increase refresh interval:
   ```json
   {
     "portMonitor.intervalMs": 5000
   }
   ```

3. Check port permissions (some ports require sudo)

## Issue 4: Process Kill Not Working

**Symptoms**: "Kill Process" option doesn't terminate process

**Solutions**:
1. Ensure feature is enabled:
   ```json
   {
     "portMonitor.enableProcessKill": true
   }
   ```

2. Check process permissions (may need sudo for system processes)

3. Use manual kill:
   ```bash
   lsof -ti :5173 | xargs kill -9
   ```
