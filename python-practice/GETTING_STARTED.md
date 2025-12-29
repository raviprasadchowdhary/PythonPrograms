# Getting Started with Python Practice

Welcome to your Python learning journey! This guide will help you set up your environment and start solving problems.

---

## 🚀 Quick Setup (5 minutes)

### 1. Create Virtual Environment

```powershell
# Navigate to project directory
cd C:\Users\916992\github\pythonPrograms\python-practice

# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\Activate.ps1
```

If you get an error about execution policies:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 2. Install Dependencies

```powershell
# Upgrade pip first
python -m pip install --upgrade pip

# Install all dependencies
pip install -r requirements.txt
```

### 3. Verify Setup

```powershell
# Run the sample tests
pytest tests/unit/test_week01_basics/test_stats.py -v

# You should see 4 tests pass! ✅
```

---

## 📖 Your First Problem

### Problem 1: Sum & Average (Already Implemented!)

The first problem is already solved as an example. Let's understand it:

1. **Open the solution:** `src/week01_basics/stats.py`
2. **Read the tests:** `tests/unit/test_week01_basics/test_stats.py`
3. **Run the tests:**
   ```powershell
   pytest tests/unit/test_week01_basics/test_stats.py -v
   ```

### Your Turn: Problem 4 (Anagram Checker)

Let's solve your first problem!

#### Step 1: Read the Problem
Open `src/week01_basics/anagram.py` - you'll see the function signature and TODO.

#### Step 2: Understand Requirements
- Input: Two strings
- Output: True if anagrams, False otherwise
- Ignore case and spaces
- Examples: "listen" ↔ "silent" = True

#### Step 3: Write the Solution

```python
def is_anagram(s1: str, s2: str) -> bool:
    # Remove spaces and convert to lowercase
    clean1 = s1.replace(" ", "").lower()
    clean2 = s2.replace(" ", "").lower()
    
    # Sort and compare
    return sorted(clean1) == sorted(clean2)
```

#### Step 4: Create Tests
Create `tests/unit/test_week01_basics/test_anagram.py`:

```python
import pytest
from src.week01_basics.anagram import is_anagram

@pytest.mark.parametrize("s1,s2,expected", [
    ("listen", "silent", True),
    ("hello", "world", False),
    ("The Eyes", "They See", True),
    ("", "", True),
])
def test_is_anagram(s1, s2, expected):
    assert is_anagram(s1, s2) == expected
```

#### Step 5: Run Your Tests

```powershell
pytest tests/unit/test_week01_basics/test_anagram.py -v
```

---

## 🎯 Recommended Learning Path

### Week 1: Basics (Problems 1-10)
Start here! Build confidence with:
- ✅ Problem 1: Stats (already done - study it!)
- ✅ Problem 2: RLE Compress (already done - study it!)
- ✅ Problem 3: Palindrome (already done - study it!)
- 📝 Problem 4: Anagram (your first!)
- 📝 Problem 5: Unique Order
- 📝 Problem 6: Flatten List
- 📝 Problem 7: Frequency Counter
- 📝 Problem 8: Rotate List
- 📝 Problem 9: Matrix Transpose
- 📝 Problem 10: FizzBuzz

**Goal:** Complete 2 problems per day = Done in 5 days!

### Daily Routine (45 minutes)

1. **Read the problem** (5 min)
   - Understand requirements
   - Check examples in `docs/problems.md`

2. **Plan your approach** (5 min)
   - What data structures?
   - What's the algorithm?
   - Edge cases?

3. **Implement solution** (20 min)
   - Write the code
   - Run it manually first

4. **Write tests** (10 min)
   - Cover happy path
   - Test edge cases
   - Use parametrize for multiple cases

5. **Verify & Refactor** (5 min)
   - Run tests: `pytest -v`
   - Check coverage: `pytest --cov=src`
   - Improve if needed

---

## 🛠️ Useful Commands

### Running Tests

```powershell
# All tests
pytest

# Specific file
pytest tests/unit/test_week01_basics/test_stats.py

# Specific test
pytest tests/unit/test_week01_basics/test_stats.py::TestStats::test_stats_valid_input

# Verbose output
pytest -v

# Stop on first failure
pytest -x

# Show print statements
pytest -s

# Fast tests only
pytest -m "not slow"

# With coverage
pytest --cov=src --cov-report=html
```

### Code Formatting

```powershell
# Format all code
black src tests

# Check imports
isort src tests

# Both together
black src tests; isort src tests
```

### Running Solutions Directly

```powershell
# Run a problem's example
python src/week01_basics/stats.py
python src/week01_basics/palindrome.py
```

---

## 📚 Learning Resources

### Documentation (in this project)
- [Full Problem List](docs/problems.md) - All 50 problems
- [Patterns Guide](docs/patterns.md) - Algorithms & data structures
- [Regex Cheatsheet](docs/cheatsheets/regex.md)
- [Pytest Cheatsheet](docs/cheatsheets/pytest.md)
- [Complexity Guide](docs/cheatsheets/complexity.md)

### External Resources
- [Python Docs](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
- [Pytest Docs](https://docs.pytest.org/)

---

## 🐛 Troubleshooting

### Virtual Environment Not Activating
```powershell
# Try this:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

### Import Errors in Tests
Make sure you're running pytest from the project root:
```powershell
cd C:\Users\916992\github\pythonPrograms\python-practice
pytest
```

### pytest Not Found
```powershell
# Make sure venv is activated
.\venv\Scripts\Activate.ps1

# Reinstall
pip install -r requirements.txt
```

---

## 🎓 Tips for Success

1. **Start Small:** Don't skip the easy problems. They build foundational skills.

2. **Write Tests First (TDD):** Try writing tests before implementation sometimes.

3. **Study the Examples:** Problems 1-3 are complete - study them!

4. **Use the REPL:** Test ideas in Python interactive mode (`python`).

5. **Read Others' Code:** After solving, look up alternative solutions online.

6. **Track Progress:** Update `docs/index.md` daily.

7. **Ask for Help:** Use the test output to guide debugging.

8. **Commit Often:** Use git to save your progress:
   ```powershell
   git add .
   git commit -m "Solved Problem 4: Anagram Checker"
   ```

---

## 🎉 Next Steps

1. ✅ **Complete setup** (you just did this!)
2. 📖 **Study Problem 1-3** (already implemented)
3. 💻 **Solve Problem 4** (your first one!)
4. 🎯 **Continue with Week 1** (Problems 5-10)
5. 📊 **Track your progress** in `docs/index.md`

---

## 💬 Need Help?

- Check the test output - it shows what's expected
- Review the cheatsheets in `docs/cheatsheets/`
- Study similar solved problems
- Read the pattern guides in `docs/patterns.md`

**Happy Coding! 🚀**

You've got this! Remember: consistent practice beats intensity. Even 30 minutes a day will get you through all 50 problems in 5 weeks.

