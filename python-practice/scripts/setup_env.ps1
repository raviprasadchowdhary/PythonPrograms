# PowerShell script to setup development environment
# Usage: .\scripts\setup_env.ps1

Write-Host "Setting up Python development environment..." -ForegroundColor Cyan

# Create virtual environment
Write-Host "Creating virtual environment..." -ForegroundColor Yellow
python -m venv venv

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

# Upgrade pip
Write-Host "Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

# Install pre-commit hooks
Write-Host "Installing pre-commit hooks..." -ForegroundColor Yellow
pre-commit install

Write-Host "`n✅ Environment setup complete!" -ForegroundColor Green
Write-Host "To activate: .\venv\Scripts\Activate.ps1" -ForegroundColor Cyan

