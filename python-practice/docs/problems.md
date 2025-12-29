# 50 Python Practice Problems

A curated set of **50 Python practice problems**—progressively structured from fundamentals to practical automation helpers. Each item includes a short brief and the **key concept(s)** it strengthens. Most use standard library only, so you can run them anywhere.

> 🧭 **How to use this:**
> Work through in order, or pick by category. Aim to write tests for your functions with **pytest** where applicable—this will align with your automation goals.

---

## 1) Core Syntax & Data Types (Basics)

1.  **Sum & Average of a List**
    *Write a function `stats(nums)` returning `(sum, avg)`.*
    *Concepts*: loops, arithmetic, list.

2.  **String Compression (Run-Length)**
    *Compress `"aaabbc"` → `"a3b2c1"`.*
    *Concepts*: loops, string building.

3.  **Palindrome Checker**
    *Ignore spaces/punctuation; `"A man, a plan, a canal: Panama"` → True.*
    *Concepts*: normalization, slicing.

4.  **Anagram Checker**
    *`"listen" vs "silent"` → True (ignore case & spaces).*
    *Concepts*: sorting/counters.

5.  **Unique Elements Preserving Order**
    *Input: `[1,2,2,3,1]` → `[1,2,3]`.*
    *Concepts*: sets, order tracking.

6.  **Flatten Nested List (One Level)**
    *`[[1,2],[3],[4,5]]` → `[1,2,3,4,5]`.*
    *Concepts*: list comprehension.

7.  **Frequency Counter**
    *Return dict of character frequencies for a string.*
    *Concepts*: `dict`, `collections.Counter`.

8.  **Rotate List Right by k**
    *`[1,2,3,4,5]`, `k=2` → `[4,5,1,2,3]`.*
    *Concepts*: slicing, modulo.

9.  **Matrix Transpose**
    *Transpose a 2D list.*
    *Concepts*: nested loops, `zip`.

10. **FizzBuzz Variant**
    *Return numbers 1..n replacing multiples of 3→"Fizz", 5→"Buzz", both→"FizzBuzz".*
    *Concepts*: conditionals, loops.

---

## 2) Functions, Errors & I/O

11. **Safe Division with Exceptions**
    *`safe_div(a,b)` returns `None` if `b==0`; else `a/b`.*
    *Concepts*: try/except, error handling.

12. **CLI Args Parser (Basic)**
    *Read two integers from `sys.argv` and print their sum.*
    *Concepts*: `sys.argv`.

13. **Read & Write Text File**
    *Count lines, words, characters; write a summary report.*
    *Concepts*: file I/O, context managers.

14. **CSV Reader & Aggregator**
    *Read prices from `data.csv`, output total per category.*
    *Concepts*: `csv` module, dicts.

15. **JSON Settings Loader**
    *Load `config.json`; provide defaults if keys missing.*
    *Concepts*: `json`, defaults, validation.

16. **Find & Replace in Files**
    *Replace all occurrences of a word across files in a folder.*
    *Concepts*: `os`, recursion, file I/O.

17. **Environment Variable Reader**
    *Read `APP_ENV`; fall back to `"dev"`.*
    *Concepts*: `os.environ`.

18. **Binary File Copy with Buffer**
    *Copy a large file efficiently—measure time.*
    *Concepts*: binary I/O, `time`.

19. **Log Rotator**
    *If log exceeds N bytes, rotate and archive with timestamp.*
    *Concepts*: file size, renaming.

20. **Regex Email Extractor**
    *Find all emails in a text using `re`.*
    *Concepts*: regex patterns, groups.

---

## 3) Data Structures & Algorithms

21. **Two Sum**
    *Return indices of two numbers that add up to target.*
    *Concepts*: hashing, time complexity.

22. **Valid Parentheses**
    *Check balanced parentheses using stack.*
    *Concepts*: stack, mapping.

23. **Merge Intervals**
    *Merge overlapping intervals, e.g., `[(1,3),(2,6),(8,10)]`.*
    *Concepts*: sorting, merging.

24. **Binary Search**
    *Implement iterative & recursive search in sorted list.*
    *Concepts*: algorithms, recursion.

25. **Linked List (Minimal)**
    *Build singly linked list with insert/delete/traverse.*
    *Concepts*: classes, pointers (references).

26. **LRU Cache**
    *Implement LRU with `OrderedDict` or custom doubly linked list.*
    *Concepts*: caching, DS design.

27. **Top-K Frequent Elements**
    *Return k most frequent numbers.*
    *Concepts*: heap, `Counter`.

28. **Word Ladder (BFS)**
    *Transform `"hit"`→`"cog"` by changing one letter at a time.*
    *Concepts*: BFS, graphs.

29. **Longest Substring Without Repeat**
    *Sliding window to find length.*
    *Concepts*: window, set/dict.

30. **Matrix Paths (DP)**
    *Count unique paths from top-left to bottom-right (no obstacles).*
    *Concepts*: dynamic programming.

---

## 4) OOP & Design

31. **Bank Account Class**
    *Deposit, withdraw (with validation), balance; use properties.*
    *Concepts*: classes, encapsulation.

32. **Shape Hierarchy**
    *`Shape` base; `Circle`, `Rectangle` with `area()`/`perimeter()`.*
    *Concepts*: inheritance, polymorphism.

33. **Observer Pattern (Events)**
    *Simple event bus: subscribe, unsubscribe, notify.*
    *Concepts*: design patterns.

34. **Context Manager (Timer)**
    *`with Timer():` prints code block duration.*
    *Concepts*: `__enter__`/`__exit__`.

35. **Singleton (Safe)**
    *Implement singleton via metaclass or module-level instance.*
    *Concepts*: metaclass / pattern trade-offs.

36. **DataClass for DTO**
    *Use `@dataclass` for immutable config object (`frozen=True`).*
    *Concepts*: dataclasses, immutability.

37. **Custom Iterator**
    *Create an iterator for Fibonacci numbers upto n.*
    *Concepts*: `__iter__`, `__next__`.

38. **Operator Overloading**
    *Vector class supporting `+`, `-`, magnitude, equality.*
    *Concepts*: `__add__`, `__eq__`.

39. **Mixin for Logging**
    *Mixin adding `log()` to multiple classes.*
    *Concepts*: mixins, composition.

40. **Plugin Architecture (Entry Points Simulated)**
    *Discover and run "plugins" from a folder by naming convention.*
    *Concepts*: importlib, discovery.

---

## 5) Concurrency, Async, & Performance

41. **Threaded Downloader (Simulated)**
    *Use `threading` to download (simulate via sleep) N tasks in parallel; collect times.*
    *Concepts*: threads, synchronization.

42. **Multiprocessing Sum of Large List**
    *Split work across processes; compare speed vs single process.*
    *Concepts*: `multiprocessing`, queues/pools.

43. **Async Rate Limiter**
    *Implement `asyncio` function that ensures at most X tasks per second.*
    *Concepts*: asyncio, semaphore.

44. **Producer–Consumer Queue**
    *Threads producing items; consumers processing; graceful shutdown.*
    *Concepts*: `queue.Queue`, signaling.

45. **Memoization Decorator**
    *Cache function results; time savings on repeated calls.*
    *Concepts*: decorators, caching.

46. **Retry with Exponential Backoff**
    *Decorator to retry flaky function with increasing wait.*
    *Concepts*: decorators, robustness.

47. **Profiler & Optimization**
    *Profile a slow function with `cProfile`, optimize it; show metrics.*
    *Concepts*: profiling, complexity.

48. **Async Task Cancellation**
    *Start multiple coroutines; cancel on timeout; handle `CancelledError`.*
    *Concepts*: asyncio cancellation.

49. **Parallel Map (ThreadPool/ProcessPool)**
    *Implement `parallel_map(func, iterable, workers)`; measure throughput.*
    *Concepts*: executors, performance.

50. **Configurable CLI Tool**
    *Build a CLI with `argparse` that runs any of the above utilities via subcommands.*
    *Concepts*: `argparse`, modularization.

---

## 🧪 Bonus: Make it "pytest-ready"

For any problem above, add:

*   A `tests/` folder with `test_<topic>.py`.
*   Use **fixtures** to supply inputs (e.g., temporary files via `tmp_path`).
*   Add markers like `@pytest.mark.slow` for performance tasks.
*   Collect coverage with `pytest --maxfail=1 --disable-warnings -q`.

**Example template (Problem #21 – Two Sum)**

```python
# two_sum.py
def two_sum(nums, target):
    index = {}
    for i, n in enumerate(nums):
        if target - n in index:
            return index[target - n], i
        index[n] = i
    return None
```

```python
# tests/test_two_sum.py
import pytest
from two_sum import two_sum

@pytest.mark.parametrize("nums,target,expected", [
    ([2,7,11,15], 9, (0,1)),
    ([3,2,4], 6, (1,2)),
    ([1,5,3], 2, None),
])
def test_two_sum(nums, target, expected):
    assert two_sum(nums, target) == expected
```

---

## 📅 Suggested 5-week plan (10 problems/week)

*   **Week 1:** 1–10 (syntax, strings, lists, control flow)
*   **Week 2:** 11–20 (I/O, files, regex, CLI)
*   **Week 3:** 21–30 (algorithms & DS)
*   **Week 4:** 31–40 (OOP & design)
*   **Week 5:** 41–50 (concurrency, async, performance)

