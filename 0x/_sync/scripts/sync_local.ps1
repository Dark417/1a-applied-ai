# sync_local.ps1 — mirror 0x/ from one exact GitHub commit into the local repo clone,
# WITHOUT git pull (the rest of D:\1AL\1a-applied-ai is left alone).
#
#   powershell -NoProfile -ExecutionPolicy Bypass -File sync_local.ps1 -Sha <commit> [-Dest D:\1AL\1a-applied-ai\0x] [-DryRun]
#
# Uses a pinned commit SHA, not "main": codeload caches the main tarball.
# robocopy /MIR = renamed/removed topic files are removed locally too.
# 0x/ is generated content: hand edits there are overwritten (edit via Cowork instead).
param(
  [Parameter(Mandatory)][string]$Sha,
  [string]$Dest = "D:\1AL\1a-applied-ai\0x",
  [string]$Repo = "Dark417/1a-applied-ai",
  [switch]$DryRun
)
$ErrorActionPreference = "Stop"
$tmp = Join-Path $env:TEMP ("0x-sync-" + $Sha.Substring(0, 7))
if (Test-Path $tmp) { Remove-Item $tmp -Recurse -Force }
New-Item -ItemType Directory -Path $tmp | Out-Null
$zip = Join-Path $tmp "src.zip"
Invoke-WebRequest -UseBasicParsing -Uri "https://codeload.github.com/$Repo/zip/$Sha" -OutFile $zip
Expand-Archive -Path $zip -DestinationPath $tmp
$src = Get-ChildItem $tmp -Directory | Where-Object { $_.Name -like "*-$Sha" } | Select-Object -First 1
$src0x = Join-Path $src.FullName "0x"
if (-not (Test-Path $src0x)) { Write-Output "NO_0X_IN_COMMIT"; exit 2 }

$args = @($src0x, $Dest, "/MIR", "/XD", "raw", "/NJH", "/NP", "/NDL")
if ($DryRun) { $args += "/L" }
& robocopy @args | Where-Object { $_ -match '\S' } | Select-Object -Last 25
$code = $LASTEXITCODE
Remove-Item $tmp -Recurse -Force
if ($code -ge 8) { Write-Output "ROBOCOPY_FAILED $code"; exit 3 }
Write-Output ("SYNCED " + $Sha.Substring(0, 7) + " -> " + $Dest + $(if ($DryRun) { " (dry run)" } else { "" }))
