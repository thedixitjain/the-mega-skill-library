<#
.SYNOPSIS
    Detects DbgViewCli.exe on the system.

.DESCRIPTION
    Searches PATH, common Sysinternals installation directories, and the
    Windows Apps folder for dbgviewcli.exe. Returns the full path if found,
    or exits with code 1 if not found.

.OUTPUTS
    The absolute path to dbgviewcli.exe if found.

.EXAMPLE
    .\detect-dbgview.ps1
    C:\Tools\dbgviewcli.exe
#>
[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'

$candidates = @(
    # 1. Check PATH
    (Get-Command 'dbgviewcli.exe' -ErrorAction SilentlyContinue)?.Source

    # 2. Common Sysinternals locations
    "$env:ProgramFiles\Sysinternals\dbgviewcli.exe"
    "$env:ProgramFiles\SysinternalsSuite\dbgviewcli.exe"
    "C:\Tools\dbgviewcli.exe"
    "C:\SysinternalsSuite\dbgviewcli.exe"
    "$env:LOCALAPPDATA\Microsoft\WindowsApps\dbgviewcli.exe"
)

$foundButUntrusted = $false

foreach ($path in $candidates) {
    if ($path -and (Test-Path -LiteralPath $path)) {
        $sig = Get-AuthenticodeSignature -FilePath $path
        if ($sig.Status -ne 'Valid' -or $sig.SignerCertificate.Subject -notlike '*Microsoft Corporation*') {
            Write-Warning "SKIPPED: '$path' is not signed by Microsoft Corporation."
            $foundButUntrusted = $true
            continue
        }
        Write-Output $path
        exit 0
    }
}

if ($foundButUntrusted) {
    Write-Error "dbgviewcli.exe found but no candidate was signed by Microsoft Corporation."
} else {
    Write-Error "dbgviewcli.exe not found. Place it in PATH or a standard Sysinternals directory."
}
exit 1
