<#
.SYNOPSIS
    End-to-end boot-time debug logging workflow.

.DESCRIPTION
    Manages the full lifecycle of boot-time kernel debug logging:
    1. Enable boot logging (requires Administrator)
    2. Optionally prompt for reboot
    3. After reboot, read captured boot log
    4. Disable boot logging

.PARAMETER Action
    The workflow step to perform: Enable, Status, Read, Disable, or Full.
    - Enable: Configure boot-time driver loading
    - Status: Check if boot logging is currently enabled
    - Read:   Read captured boot log after reboot
    - Disable: Remove boot-time driver configuration
    - Full:   Interactive full workflow (enable → prompt reboot → read → disable)

.PARAMETER OutputFile
    Path to save boot log output. Default: .\boot-debug-output.log

.PARAMETER Format
    Output format for reading boot log: text, csv, or xml. Default: text.

.EXAMPLE
    .\boot-logging-workflow.ps1 -Action Enable

.EXAMPLE
    .\boot-logging-workflow.ps1 -Action Read -OutputFile .\boot.csv -Format csv

.EXAMPLE
    .\boot-logging-workflow.ps1 -Action Full
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [ValidateSet('Enable', 'Status', 'Read', 'Disable', 'Full')]
    [string]$Action,

    [string]$OutputFile = '.\boot-debug-output.log',

    [ValidateSet('text', 'csv', 'xml')]
    [string]$Format = 'text'
)

$ErrorActionPreference = 'Stop'

# Require elevation for all boot logging operations
$identity = [Security.Principal.WindowsIdentity]::GetCurrent()
$principal = [Security.Principal.WindowsPrincipal]$identity
if (-not $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Error "Boot logging operations require Administrator privileges."
    exit 1
}

# Detect binary
$dbgviewcli = & "$PSScriptRoot\detect-dbgview.ps1"

function Invoke-Enable {
    Write-Host "Enabling boot-time kernel debug logging..." -ForegroundColor Cyan
    & $dbgviewcli --boot-enable
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Boot logging enabled. Reboot to capture boot-time debug output." -ForegroundColor Green
    } else {
        Write-Error "Failed to enable boot logging (exit code: $LASTEXITCODE)."
    }
}

function Invoke-Status {
    Write-Host "Checking boot logging status..." -ForegroundColor Cyan
    & $dbgviewcli --boot-status
}

function Invoke-Read {
    Write-Host "Reading boot debug output..." -ForegroundColor Cyan
    $readArgs = @('--no-banner', '--format', $Format)
    if ($OutputFile) {
        $readArgs += '--log', $OutputFile
    }
    # Boot log is captured by the driver; use kernel read to retrieve it
    & $dbgviewcli @readArgs --kernel --duration 5
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Failed to read boot log (exit code: $LASTEXITCODE)."
        return
    }
    if (Test-Path $OutputFile) {
        Write-Host "Boot log saved to: $OutputFile" -ForegroundColor Green
    }
}

function Invoke-Disable {
    Write-Host "Disabling boot-time kernel debug logging..." -ForegroundColor Cyan
    & $dbgviewcli --boot-disable
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Boot logging disabled." -ForegroundColor Green
    } else {
        Write-Error "Failed to disable boot logging (exit code: $LASTEXITCODE)."
    }
}

switch ($Action) {
    'Enable'  { Invoke-Enable }
    'Status'  { Invoke-Status }
    'Read'    { Invoke-Read }
    'Disable' { Invoke-Disable }
    'Full' {
        Invoke-Enable
        Write-Host ""
        Write-Host "Please reboot the system to capture boot-time debug output." -ForegroundColor Yellow
        Write-Host "After reboot, run this script again with: -Action Read" -ForegroundColor Yellow
        Write-Host "When finished, run with: -Action Disable" -ForegroundColor Yellow
    }
}
