# Pytest Cheatsheet

Quick reference for pytest testing framework.

---

## 🚀 Installation

```bash
pip install pytest pytest-cov pytest-asyncio
```

---

## 📝 Basic Test

```python
# test_example.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

Run: `pytest test_example.py`

---

## 🎯 Assertions

```python
# Basic assertions
assert value
assert value == expected
assert value != other
assert value in collection
assert value is None
assert value is not None

# With messages
assert value == expected, f"Expected {expected}, got {value}"

# Approximate comparison
assert abs(0.1 + 0.2 - 0.3) < 1e-10
# or
import pytest
assert 0.1 + 0.2 == pytest.approx(0.3)

# Exception assertions
with pytest.raises(ValueError):
    int('invalid')

with pytest.raises(ValueError, match=r'invalid'):
    int('invalid')
```

---

## 🏷️ Markers

### Built-in Markers
```python
import pytest

@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    pass

@pytest.mark.skipif(sys.version_info < (3, 10), reason="Requires Python 3.10+")
def test_new_syntax():
    pass

@pytest.mark.xfail(reason="Known bug")
def test_known_issue():
    assert False

@pytest.mark.slow
def test_performance():
    # Long-running test
    pass
```

### Custom Markers (in pytest.ini)
```ini
[pytest]
markers =
    slow: marks tests as slow
    integration: integration tests
    unit: unit tests
```

Run specific markers:
```bash
pytest -m slow          # Run slow tests
pytest -m "not slow"    # Skip slow tests
pytest -m "unit and not slow"
```

---

## 🎨 Parametrize

```python
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# Multiple parameters
@pytest.mark.parametrize("x", [1, 2, 3])
@pytest.mark.parametrize("y", [10, 20])
def test_combinations(x, y):
    assert x < y  # Runs 6 times (3 × 2)

# IDs for better output
@pytest.mark.parametrize("input,expected", [
    ("hello", "HELLO"),
    ("World", "WORLD"),
], ids=["lowercase", "mixedcase"])
def test_upper(input, expected):
    assert input.upper() == expected
```

---

## 🔧 Fixtures

### Basic Fixture
```python
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    assert sum(sample_data) == 15
```

### Setup/Teardown
```python
@pytest.fixture
def database():
    # Setup
    db = connect_to_db()
    yield db
    # Teardown
    db.close()

def test_query(database):
    result = database.query("SELECT 1")
    assert result is not None
```

### Scope
```python
@pytest.fixture(scope="function")  # Default: per test
def func_fixture():
    pass

@pytest.fixture(scope="class")  # Per test class
def class_fixture():
    pass

@pytest.fixture(scope="module")  # Per module
def module_fixture():
    pass

@pytest.fixture(scope="session")  # Per test session
def session_fixture():
    pass
```

### Built-in Fixtures
```python
def test_temp_files(tmp_path):
    """tmp_path: Path object for temp directory"""
    file = tmp_path / "test.txt"
    file.write_text("hello")
    assert file.read_text() == "hello"

def test_temp_dir(tmpdir):
    """tmpdir: Legacy temp directory (use tmp_path instead)"""
    pass

def test_capture_output(capsys):
    """capsys: Capture stdout/stderr"""
    print("Hello")
    captured = capsys.readouterr()
    assert captured.out == "Hello\n"

def test_monkeypatch(monkeypatch):
    """monkeypatch: Modify objects/environment"""
    monkeypatch.setenv("API_KEY", "test")
    monkeypatch.setattr(module, "function", lambda: "mocked")
```

### Fixture in conftest.py
```python
# tests/conftest.py
import pytest

@pytest.fixture
def shared_fixture():
    """Available to all tests in directory and subdirectories"""
    return {"key": "value"}
```

---

## 📁 Test Organization

```
tests/
├── conftest.py           # Shared fixtures
├── unit/
│   ├── conftest.py       # Unit-specific fixtures
│   ├── test_module1.py
│   └── test_module2.py
└── integration/
    ├── conftest.py
    └── test_api.py
```

---

## 🎭 Mocking

```python
from unittest.mock import Mock, patch, MagicMock

# Mock object
def test_with_mock():
    mock_db = Mock()
    mock_db.query.return_value = [1, 2, 3]
    
    result = mock_db.query("SELECT *")
    assert result == [1, 2, 3]
    mock_db.query.assert_called_once_with("SELECT *")

# Patch
@patch('module.external_api')
def test_with_patch(mock_api):
    mock_api.return_value = {"status": "ok"}
    
    result = module.call_api()
    assert result["status"] == "ok"

# Context manager
def test_patch_context():
    with patch('module.function') as mock_func:
        mock_func.return_value = 42
        assert module.function() == 42
```

---

## 🔄 Async Tests

```python
import pytest

@pytest.mark.asyncio
async def test_async_function():
    result = await async_add(2, 3)
    assert result == 5

# Async fixture
@pytest.fixture
async def async_client():
    client = await create_client()
    yield client
    await client.close()

@pytest.mark.asyncio
async def test_with_async_fixture(async_client):
    result = await async_client.get("/api")
    assert result.status == 200
```

---

## 📊 Coverage

```bash
# Run with coverage
pytest --cov=src

# HTML report
pytest --cov=src --cov-report=html

# Specific module
pytest --cov=src.module --cov-report=term-missing

# Fail if coverage below threshold
pytest --cov=src --cov-fail-under=80
```

---

## 🎮 Command-Line Options

```bash
# Verbose output
pytest -v

# Show print statements
pytest -s

# Run specific test
pytest tests/test_module.py::test_function
pytest tests/test_module.py::TestClass::test_method

# Run by keyword
pytest -k "test_add"
pytest -k "not slow"

# Stop after first failure
pytest -x

# Stop after N failures
pytest --maxfail=3

# Show locals on failure
pytest -l

# Run last failed tests
pytest --lf

# Run failed first, then others
pytest --ff

# Parallel execution (requires pytest-xdist)
pytest -n 4

# Quiet mode
pytest -q

# Show slowest tests
pytest --durations=10
```

---

## ⚙️ Configuration (pytest.ini)

```ini
[pytest]
minversion = 7.0
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*

addopts =
    -ra
    --strict-markers
    --strict-config
    --showlocals
    -v

markers =
    slow: marks tests as slow
    integration: integration tests
    unit: unit tests

filterwarnings =
    error
    ignore::DeprecationWarning
```

---

## 🎯 Best Practices

1. **Naming:** Use `test_` prefix for files and functions
2. **One assert per test:** When possible (or related asserts)
3. **AAA pattern:** Arrange, Act, Assert
   ```python
   def test_example():
       # Arrange
       data = [1, 2, 3]
       
       # Act
       result = sum(data)
       
       # Assert
       assert result == 6
   ```
4. **Use fixtures:** Share setup code
5. **Parametrize:** Test multiple inputs
6. **Descriptive names:** `test_add_positive_numbers`
7. **Test edge cases:** Empty, None, negative, large values

---

## 🧪 Example Test Suite

```python
# tests/test_calculator.py
import pytest
from calculator import Calculator

class TestCalculator:
    @pytest.fixture
    def calc(self):
        return Calculator()
    
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
    ])
    def test_add(self, calc, a, b, expected):
        assert calc.add(a, b) == expected
    
    def test_divide_by_zero(self, calc):
        with pytest.raises(ZeroDivisionError):
            calc.divide(10, 0)
    
    @pytest.mark.slow
    def test_performance(self, calc):
        """Test with large numbers"""
        result = calc.add(10**9, 10**9)
        assert result == 2 * 10**9
```

---

## 📚 Useful Plugins

```bash
pip install pytest-cov          # Coverage reporting
pip install pytest-asyncio      # Async support
pip install pytest-xdist        # Parallel execution
pip install pytest-timeout      # Timeout for tests
pip install pytest-mock         # Better mocking
pip install pytest-benchmark   # Benchmarking
```

---

## 🔗 Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Pytest Good Practices](https://docs.pytest.org/en/stable/goodpractices.html)

