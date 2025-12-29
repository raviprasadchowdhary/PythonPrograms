# PowerShell script to run all tests
# Usage: .\scripts\run_all.ps1

Write-Host "Running all tests..." -ForegroundColor Cyan
pytest -v

