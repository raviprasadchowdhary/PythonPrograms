# Python Practice - 50 Problems Journey

A structured learning path to master Python fundamentals, data structures, algorithms, OOP, and concurrency—tailored for Playwright + Pytest automation.

## 🎯 Goals

- Build strong Python fundamentals
- Learn data structures & algorithms
- Master OOP and design patterns
- Understand concurrency & async programming
- Practice test-driven development with pytest

## 📂 Project Structure

```
python-practice/
├── src/              # Source code organized by week/topic
├── tests/            # Pytest test suites
├── docs/             # Documentation and learning notes
├── scripts/          # Helper scripts
└── data/             # Sample data files for testing
```

## 🚀 Quick Start

### Setup Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific week
pytest tests/unit/test_week01_basics/

# Run fast tests only
pytest -m "not slow"
```

## 📅 5-Week Learning Plan

- **Week 1:** Core Syntax & Data Types (Problems 1-10)
- **Week 2:** Functions, Errors & I/O (Problems 11-20)
- **Week 3:** Data Structures & Algorithms (Problems 21-30)
- **Week 4:** OOP & Design Patterns (Problems 31-40)
- **Week 5:** Concurrency, Async & Performance (Problems 41-50)

## 📖 Documentation

- [Full Problem List](docs/problems.md) - All 50 problems with descriptions
- [Patterns & Notes](docs/patterns.md) - DS/Algo patterns reference
- [Cheatsheets](docs/cheatsheets/) - Quick references

## 🧪 Testing Philosophy

All solutions include:
- Unit tests with pytest
- Parametrized test cases
- Edge case coverage
- Performance markers for slow tests

## 🛠️ Tools & Technologies

- **Python 3.10+**
- **pytest** - Testing framework
- **black** - Code formatting
- **isort** - Import sorting
- **mypy** - Type checking (optional)
- **pre-commit** - Git hooks for code quality

## 📊 Progress Tracking

Track your progress in [docs/index.md](docs/index.md)

## 🤝 Contributing

This is a personal learning repository, but feel free to use it as a template for your own journey!

## 📝 License

MIT License - feel free to use for learning purposes.

