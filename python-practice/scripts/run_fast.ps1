# PowerShell script to run fast tests only
# Usage: .\scripts\run_fast.ps1

Write-Host "Running fast tests only..." -ForegroundColor Cyan
pytest -m "not slow and not performance" -v

