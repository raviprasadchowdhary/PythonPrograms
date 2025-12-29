#!/bin/bash
# Setup development environment

echo "Setting up Python development environment..."

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Install pre-commit hooks
pre-commit install

echo "✅ Environment setup complete!"
echo "To activate: source venv/bin/activate"

