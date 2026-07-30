<#
.SYNOPSIS
    Convenience wrapper for common DbgViewCli agent capture patterns.

.DESCRIPTION
    Provides a safe, bounded capture invocation suitable for AI agent use.
    Always enforces --no-banner and at least one bound (--duration or --max-lines).

.PARAMETER Duration
    Maximum capture duration in seconds. Default: 30.

.PARAMETER MaxLines
    Maximum number of lines to capture. Default: 0 (unlimited, but Duration still applies).

.PARAMETER Filter
    Include filter pattern (semicolon-separated wildcards).

.PARAMETER Exclude
    Exclude filter pattern (semicolon-separated wildcards).

.PARAMETER PidFilter
    Filter by specific process ID.

.PARAMETER ProcessFilter
    Filter by process name (substring match).

.PARAMETER WaitFor
    Stop capture when this wildcard pattern matches.

.PARAMETER Tail
    Only output the last N lines on exit.

.PARAMETER Format
    Output format: text, csv, or xml. Default: text.

.PARAMETER LogFile
    Path to log file. If specified, output is also written to this file.

.PARAMETER Kernel
    Enable kernel-mode debug capture (requires Administrator).

.EXAMPLE
    .\capture-wrapper.ps1 -Duration 60 -ProcessFilter "myapp.exe"

.EXAMPLE
    .\capture-wrapper.ps1 -Duration 120 -Kernel -Format csv -LogFile .\kernel.csv
#>
[CmdletBinding()]
param(
    [int]$Duration = 30,
    [int]$MaxLines = 0,
    [string]$Filter,
    [string]$Exclude,
    [int]$PidFilter = 0,
    [string]$ProcessFilter,
    [string]$WaitFor,
    [int]$Tail = 0,
    [ValidateSet('text', 'csv', 'xml')]
    [string]$Format = 'text',
    [string]$LogFile,
    [switch]$Kernel
)

$ErrorActionPreference = 'Stop'

# Detect binary
$dbgviewcli = & "$PSScriptRoot\detect-dbgview.ps1"

# Build argument list
$args = @('--no-banner', '--duration', $Duration)

if ($MaxLines -gt 0) { $args += '--max-lines', $MaxLines }
if ($Filter)         { $args += '--filter', $Filter }
if ($Exclude)        { $args += '--exclude', $Exclude }
if ($PidFilter -gt 0){ $args += '--pid-filter', $PidFilter }
if ($ProcessFilter)  { $args += '--process-filter', $ProcessFilter }
if ($WaitFor)        { $args += '--wait-for', $WaitFor }
if ($Tail -gt 0)     { $args += '--tail', $Tail }
if ($Format -ne 'text') { $args += '--format', $Format }
if ($LogFile)        { $args += '--log', $LogFile }
if ($Kernel)         { $args += '--kernel' }

# Elevation check for kernel capture
if ($Kernel) {
    $identity = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = [Security.Principal.WindowsPrincipal]$identity
    if (-not $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
        Write-Error "Kernel capture requires Administrator privileges. Run this script elevated."
        exit 1
    }
}

Write-Verbose "Executing: $dbgviewcli $($args -join ' ')"
& $dbgviewcli @args
