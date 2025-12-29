# Makefile for common development tasks
# Note: This is primarily for Linux/macOS. Windows users should use scripts/*.ps1

.PHONY: help install test test-fast test-cov lint format clean

help:
	@echo "Available commands:"
	@echo "  make install    - Install dependencies"
	@echo "  make test       - Run all tests"
	@echo "  make test-fast  - Run tests excluding slow ones"
	@echo "  make test-cov   - Run tests with coverage report"
	@echo "  make lint       - Run linters (black, isort, mypy)"
	@echo "  make format     - Auto-format code"
	@echo "  make clean      - Remove cache and build files"

install:
	pip install -r requirements.txt
	pre-commit install

test:
	pytest

test-fast:
	pytest -m "not slow"

test-cov:
	pytest --cov=src --cov-report=html --cov-report=term

lint:
	black --check src tests
	isort --check-only src tests
	mypy src

format:
	black src tests
	isort src tests

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache .mypy_cache htmlcov .coverage

