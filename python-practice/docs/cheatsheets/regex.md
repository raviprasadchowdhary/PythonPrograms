# Python Regex Cheatsheet

Quick reference for regular expressions in Python.

---

## 📚 Import

```python
import re
```

---

## 🔍 Basic Patterns

| Pattern | Meaning | Example |
|---------|---------|---------|
| `.` | Any character except newline | `a.c` matches "abc", "a1c" |
| `^` | Start of string | `^Hello` matches "Hello world" |
| `$` | End of string | `world$` matches "Hello world" |
| `*` | 0 or more | `ab*c` matches "ac", "abc", "abbc" |
| `+` | 1 or more | `ab+c` matches "abc", "abbc" |
| `?` | 0 or 1 | `ab?c` matches "ac", "abc" |
| `{n}` | Exactly n | `a{3}` matches "aaa" |
| `{n,}` | n or more | `a{2,}` matches "aa", "aaa" |
| `{n,m}` | Between n and m | `a{2,4}` matches "aa", "aaa", "aaaa" |

---

## 📝 Character Classes

| Pattern | Meaning |
|---------|---------|
| `[abc]` | Match a, b, or c |
| `[^abc]` | NOT a, b, or c |
| `[a-z]` | Lowercase letters |
| `[A-Z]` | Uppercase letters |
| `[0-9]` | Digits |
| `[a-zA-Z0-9]` | Alphanumeric |

---

## 🎯 Predefined Classes

| Pattern | Equivalent | Meaning |
|---------|------------|---------|
| `\d` | `[0-9]` | Digit |
| `\D` | `[^0-9]` | Non-digit |
| `\w` | `[a-zA-Z0-9_]` | Word character |
| `\W` | `[^a-zA-Z0-9_]` | Non-word character |
| `\s` | `[ \t\n\r\f\v]` | Whitespace |
| `\S` | `[^ \t\n\r\f\v]` | Non-whitespace |

---

## 🔗 Anchors & Boundaries

| Pattern | Meaning |
|---------|---------|
| `^` | Start of string/line |
| `$` | End of string/line |
| `\b` | Word boundary |
| `\B` | Not word boundary |
| `\A` | Start of string (no multiline) |
| `\Z` | End of string (no multiline) |

---

## 🎭 Groups & Lookarounds

### Groups
```python
# Capturing group
match = re.search(r'(\d{3})-(\d{3})-(\d{4})', '123-456-7890')
match.group(1)  # '123'
match.group(2)  # '456'

# Non-capturing group
re.search(r'(?:abc)+', 'abcabc')

# Named group
match = re.search(r'(?P<area>\d{3})-(?P<prefix>\d{3})', '123-456')
match.group('area')  # '123'
```

### Lookarounds
```python
# Positive lookahead
re.search(r'\d+(?= dollars)', '100 dollars')  # Matches '100'

# Negative lookahead
re.search(r'\d+(?! dollars)', '100 euros')  # Matches '100'

# Positive lookbehind
re.search(r'(?<=\$)\d+', '$100')  # Matches '100'

# Negative lookbehind
re.search(r'(?<!\$)\d+', '€100')  # Matches '100'
```

---

## 🛠️ Functions

### `re.search()`
Find first match anywhere in string
```python
match = re.search(r'\d+', 'Age: 25')
if match:
    print(match.group())  # '25'
```

### `re.match()`
Match at beginning of string
```python
match = re.match(r'\d+', '25 years')
```

### `re.findall()`
Find all matches, return list
```python
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
```

### `re.finditer()`
Find all matches, return iterator of match objects
```python
for match in re.finditer(r'\d+', 'a1b2c3'):
    print(match.group(), match.start(), match.end())
```

### `re.sub()`
Replace matches
```python
result = re.sub(r'\d+', 'X', 'a1b2c3')  # 'aXbXcX'

# With function
def increment(match):
    return str(int(match.group()) + 1)

result = re.sub(r'\d+', increment, 'a1b2c3')  # 'a2b3c4'
```

### `re.split()`
Split by pattern
```python
parts = re.split(r'[,;]', 'a,b;c')  # ['a', 'b', 'c']
```

---

## 🎨 Flags

```python
# Case-insensitive
re.search(r'hello', 'HELLO', re.IGNORECASE)  # or re.I

# Multiline mode (^ and $ match line boundaries)
re.search(r'^word', text, re.MULTILINE)  # or re.M

# Dot matches newline
re.search(r'a.b', 'a\nb', re.DOTALL)  # or re.S

# Verbose (ignore whitespace, allow comments)
pattern = re.compile(r'''
    \d{3}    # Area code
    -        # Separator
    \d{3}    # Prefix
    -        # Separator
    \d{4}    # Line number
''', re.VERBOSE)  # or re.X

# Combine flags
re.search(pattern, text, re.I | re.M)
```

---

## 📧 Common Patterns

### Email
```python
r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
```

### URL
```python
r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)'
```

### Phone (US)
```python
r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
```

### IP Address
```python
r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
```

### Date (YYYY-MM-DD)
```python
r'\b\d{4}-\d{2}-\d{2}\b'
```

### Hex Color
```python
r'#[0-9A-Fa-f]{6}\b'
```

---

## 💡 Best Practices

1. **Raw strings:** Always use `r''` for regex patterns
2. **Compile:** Compile patterns used multiple times
   ```python
   pattern = re.compile(r'\d+')
   pattern.findall(text)
   ```
3. **Non-greedy:** Use `*?`, `+?` for minimal matching
4. **Escape special chars:** Use `re.escape()` for literal strings
   ```python
   re.search(re.escape('$100'), text)
   ```

---

## 🧪 Testing Regex

Online tools:
- regex101.com
- pythex.org

```python
# Test pattern
pattern = r'\b\w+@\w+\.\w+\b'
test_cases = [
    'user@example.com',
    'invalid@',
    '@invalid.com',
    'good.user@test.co.uk',
]

for test in test_cases:
    match = re.search(pattern, test)
    print(f"{test}: {'✓' if match else '✗'}")
```

---

## 🔧 Problem #20: Email Extractor

```python
import re

def extract_emails(text):
    """Extract all email addresses from text."""
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

# Test
text = "Contact us at support@example.com or sales@company.org"
print(extract_emails(text))
# ['support@example.com', 'sales@company.org']
```

