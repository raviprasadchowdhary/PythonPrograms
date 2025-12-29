# Python Programs Repository

Welcome to my Python learning and practice repository! This workspace contains various Python projects and exercises for building proficiency in Python programming, particularly for test automation with Playwright and Pytest.

---

## 📁 Repository Structure

```
pythonPrograms/
├── README.md                    # This file
├── main.py                      # Sample Python script
├── topics.txt                   # Learning topics and problem list
└── python-practice/             # 🎯 Main practice project (50 problems)
    ├── README.md
    ├── GETTING_STARTED.md       # 👈 Start here for the practice project!
    ├── docs/                    # Learning materials & documentation
    ├── src/                     # Problem solutions (5 weeks)
    ├── tests/                   # Test suites with pytest
    └── scripts/                 # Helper scripts
```

---

## 🎯 Main Project: python-practice

The **python-practice** folder contains a comprehensive 5-week learning program with 50 progressively challenging Python problems.

### Quick Start

```powershell
# Navigate to the practice project
cd python-practice

# Follow the setup guide
# See python-practice/GETTING_STARTED.md for detailed instructions
```

### What's Inside

- **50 Practice Problems** organized by difficulty and topic
- **Complete solutions** for 4 problems as examples
- **Professional testing** with pytest framework
- **Comprehensive documentation** including:
  - Algorithm patterns guide
  - Regex cheatsheet
  - Pytest cheatsheet
  - Time/space complexity reference
- **Development tools** (black, isort, mypy, pre-commit)
- **CI/CD pipeline** with GitHub Actions

### Learning Path (5 Weeks)

| Week | Focus | Problems | Topics |
|------|-------|----------|--------|
| **Week 1** | Core Syntax & Data Types | 1-10 | Lists, strings, loops, conditionals |
| **Week 2** | Functions, Errors & I/O | 11-20 | File I/O, regex, exception handling |
| **Week 3** | Data Structures & Algorithms | 21-30 | Hash maps, stacks, queues, BFS/DFS |
| **Week 4** | OOP & Design Patterns | 31-40 | Classes, inheritance, design patterns |
| **Week 5** | Concurrency & Performance | 41-50 | Threading, async/await, optimization |

---

## 📚 Resources

### Documentation
- **[50 Problems List](python-practice/docs/problems.md)** - Full problem descriptions
- **[Getting Started Guide](python-practice/GETTING_STARTED.md)** - Setup and first steps
- **[Algorithm Patterns](python-practice/docs/patterns.md)** - Common patterns reference
- **[Cheatsheets](python-practice/docs/cheatsheets/)** - Quick references

### Topics Covered
- Python fundamentals (syntax, data types, control flow)
- Data structures (lists, sets, dicts, trees, graphs)
- Algorithms (sorting, searching, recursion, DP)
- Object-oriented programming
- File I/O and serialization (CSV, JSON)
- Regular expressions
- Exception handling
- Testing with pytest
- Asynchronous programming
- Concurrency (threading, multiprocessing)
- Performance optimization

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Git (for version control)

### Setup

1. **Clone the repository** (if not already done)
   ```powershell
   git clone <repository-url>
   cd pythonPrograms
   ```

2. **Navigate to the practice project**
   ```powershell
   cd python-practice
   ```

3. **Set up the environment**
   ```powershell
   # Create virtual environment
   python -m venv venv
   
   # Activate it (Windows PowerShell)
   .\venv\Scripts\Activate.ps1
   
   # Install dependencies
   pip install -r requirements.txt
   ```

4. **Verify setup**
   ```powershell
   # Run example tests
   pytest tests/unit/test_week01_basics/ -v
   ```

5. **Start learning!**
   - Read `python-practice/GETTING_STARTED.md`
   - Study the 3 example solutions
   - Begin with Problem 4 (your first challenge!)

---

## 📖 How to Use This Repository

### For Learning
1. **Follow the 5-week plan** in `python-practice/`
2. **Study example solutions** (Problems 1-3 are complete)
3. **Write tests first** using pytest
4. **Track your progress** in `docs/index.md`
5. **Review patterns** before tackling algorithms

### For Reference
- Use the **cheatsheets** for quick lookups
- Check **patterns.md** for algorithm templates
- Reference **problems.md** for problem descriptions

### For Practice
- Complete 2 problems per day
- Write comprehensive tests for each solution
- Aim for clean, readable code
- Use type hints and docstrings

---

## 🛠️ Development Tools

The python-practice project includes professional development tools:

- **pytest** - Testing framework with fixtures and parametrization
- **black** - Code formatter (PEP 8 compliant)
- **isort** - Import statement organizer
- **mypy** - Static type checker
- **pre-commit** - Git hooks for code quality
- **coverage** - Code coverage reporting

### Common Commands

```powershell
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Format code
black src tests

# Sort imports
isort src tests

# Type check
mypy src
```

---

## 🎓 Learning Goals

This repository is designed to help you:

- ✅ Master Python fundamentals and advanced concepts
- ✅ Build strong problem-solving skills
- ✅ Learn industry-standard testing practices
- ✅ Understand algorithms and data structures
- ✅ Write clean, maintainable code
- ✅ Prepare for technical interviews
- ✅ Support Playwright + Pytest automation work

---

## 📊 Progress Tracking

Track your learning journey in `python-practice/docs/index.md`:

- **Current Week:** Week 1
- **Problems Completed:** 0/50
- **Target Completion:** 5 weeks
- **Daily Goal:** 2 problems

Update your progress daily to stay motivated!

---

## 🔗 Additional Resources

### Python Documentation
- [Official Python Docs](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [PEP 8 Style Guide](https://pep8.org/)

### Learning Platforms
- [Real Python](https://realpython.com/)
- [Python.org Beginners Guide](https://wiki.python.org/moin/BeginnersGuide)
- [LeetCode](https://leetcode.com/) - Algorithm practice

### Testing Resources
- [Pytest Documentation](https://docs.pytest.org/)
- [Pytest Tutorial](https://realpython.com/pytest-python-testing/)

---

## 📝 Notes

- The `main.py` file is a sample script for quick experiments
- The `topics.txt` file contains the original problem list and ideas
- The `python-practice/` directory is the main learning project
- All practice code should be in `python-practice/src/`
- All tests should be in `python-practice/tests/`

---

## 🎯 Next Steps

1. ✅ **Read this README** - You're here! ✓
2. 📖 **Navigate to python-practice/** 
3. 📚 **Read GETTING_STARTED.md**
4. 💻 **Set up your environment**
5. 🧪 **Run the example tests**
6. 🚀 **Start solving Problem 4!**

---

## 🤝 Contributing

This is a personal learning repository. Feel free to:
- Fork it for your own learning
- Suggest improvements via issues
- Share alternative solutions

---

## 📜 License

This project is for educational purposes. Feel free to use it for your own learning.

---

## ✨ Acknowledgments

This structured learning approach is designed to build practical Python skills for test automation and software development, with a focus on real-world applications.

---

**Happy Coding! 🐍🚀**

*Last Updated: December 29, 2025*

---

## 📞 Quick Links

- **[Getting Started Guide](python-practice/GETTING_STARTED.md)** - Your first steps
- **[50 Problems List](python-practice/docs/problems.md)** - All challenges
- **[Algorithm Patterns](python-practice/docs/patterns.md)** - Solutions guide
- **[Project Overview](python-practice/README.md)** - Practice project details

---

*Ready to start? Head to `python-practice/GETTING_STARTED.md` and begin your Python journey!* 🎉

