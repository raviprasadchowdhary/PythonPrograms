# Time & Space Complexity Cheatsheet

Quick reference for algorithm complexity analysis.

---

## 📊 Big O Notation

Big O describes the **worst-case** time or space an algorithm needs.

### Common Complexities (Best to Worst)

| Notation | Name | Example | Description |
|----------|------|---------|-------------|
| O(1) | Constant | Array access, hash lookup | Same time regardless of input size |
| O(log n) | Logarithmic | Binary search | Halves the problem each step |
| O(n) | Linear | Single loop, array scan | Scales linearly with input |
| O(n log n) | Linearithmic | Merge sort, quick sort | Efficient sorting |
| O(n²) | Quadratic | Nested loops, bubble sort | Scales with square of input |
| O(n³) | Cubic | Triple nested loops | Very slow for large inputs |
| O(2ⁿ) | Exponential | Recursive Fibonacci | Doubles with each addition |
| O(n!) | Factorial | Permutations, TSP | Extremely slow |

### Visual Growth

```
Input Size (n) →    10      100     1,000   10,000
─────────────────────────────────────────────────────
O(1)                1       1       1       1
O(log n)            3       7       10      13
O(n)                10      100     1,000   10,000
O(n log n)          30      700     10,000  130,000
O(n²)               100     10,000  1M      100M
O(2ⁿ)               1,024   ∞       ∞       ∞
```

---

## ⏱️ Time Complexity Examples

### O(1) - Constant
```python
def get_first(arr):
    return arr[0]  # Always one operation

def hash_lookup(d, key):
    return d[key]  # Hash table lookup
```

### O(log n) - Logarithmic
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### O(n) - Linear
```python
def find_max(arr):
    max_val = arr[0]
    for num in arr:  # n iterations
        if num > max_val:
            max_val = num
    return max_val
```

### O(n log n) - Linearithmic
```python
def merge_sort(arr):
    # Dividing: log n levels
    # Merging: n operations per level
    # Total: n log n
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
```

### O(n²) - Quadratic
```python
def bubble_sort(arr):
    for i in range(len(arr)):      # n
        for j in range(len(arr)):  # n
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

### O(2ⁿ) - Exponential
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # Doubles each level
```

---

## 💾 Space Complexity Examples

### O(1) - Constant Space
```python
def sum_array(arr):
    total = 0  # Single variable
    for num in arr:
        total += num
    return total
```

### O(n) - Linear Space
```python
def copy_array(arr):
    return arr[:]  # New array of size n

def recursive_sum(arr, index=0):
    if index == len(arr):
        return 0
    return arr[index] + recursive_sum(arr, index+1)  # n stack frames
```

### O(log n) - Logarithmic Space
```python
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid+1, right)
    else:
        return binary_search_recursive(arr, target, left, mid-1)
    # log n recursive calls on stack
```

---

## 🔍 How to Analyze

### 1. Count Operations
```python
def example(n):
    x = 5          # O(1)
    for i in range(n):  # O(n)
        print(i)   # O(1) per iteration
    # Total: O(1) + O(n) = O(n)
```

### 2. Nested Loops
```python
def example(n):
    for i in range(n):      # O(n)
        for j in range(n):  # O(n)
            print(i, j)     # O(1)
    # Total: O(n) × O(n) = O(n²)
```

### 3. Sequential Statements
```python
def example(arr):
    do_something()      # O(n)
    do_something_else() # O(n²)
    # Total: O(n) + O(n²) = O(n²)  # Keep largest
```

### 4. Logarithmic Operations
```python
def example(n):
    i = 1
    while i < n:
        i *= 2  # Doubles each time
    # Runs log₂(n) times → O(log n)
```

---

## 📐 Rules of Thumb

### Drop Constants
- O(2n) → O(n)
- O(n/2) → O(n)
- O(3n + 5) → O(n)

### Drop Lower Terms
- O(n² + n) → O(n²)
- O(n³ + n² + n) → O(n³)

### Different Variables
```python
def example(arr1, arr2):
    for x in arr1:    # O(a)
        print(x)
    for y in arr2:    # O(b)
        print(y)
    # Total: O(a + b), NOT O(n)
```

### Nested Different Variables
```python
def example(arr1, arr2):
    for x in arr1:        # O(a)
        for y in arr2:    # O(b)
            print(x, y)
    # Total: O(a × b)
```

---

## 🎯 Data Structure Operations

| Data Structure | Access | Search | Insert | Delete | Space |
|----------------|--------|--------|--------|--------|-------|
| Array | O(1) | O(n) | O(n) | O(n) | O(n) |
| Stack | O(n) | O(n) | O(1) | O(1) | O(n) |
| Queue | O(n) | O(n) | O(1) | O(1) | O(n) |
| Linked List | O(n) | O(n) | O(1)* | O(1)* | O(n) |
| Hash Table | - | O(1)† | O(1)† | O(1)† | O(n) |
| Binary Search Tree | O(log n)‡ | O(log n)‡ | O(log n)‡ | O(log n)‡ | O(n) |
| Heap | - | O(n) | O(log n) | O(log n) | O(n) |

*With reference to node  
†Average case  
‡Balanced tree

---

## 🏆 Common Algorithm Complexities

### Sorting
- Bubble Sort: O(n²)
- Selection Sort: O(n²)
- Insertion Sort: O(n²)
- Merge Sort: O(n log n)
- Quick Sort: O(n log n) average, O(n²) worst
- Heap Sort: O(n log n)
- Counting Sort: O(n + k)

### Searching
- Linear Search: O(n)
- Binary Search: O(log n)
- Hash Table Lookup: O(1) average

### Graph Algorithms
- BFS: O(V + E)
- DFS: O(V + E)
- Dijkstra: O((V + E) log V)
- Bellman-Ford: O(VE)

---

## 💡 Optimization Tips

### Use Hash Maps
```python
# Slow: O(n²)
for i in range(len(arr)):
    if target - arr[i] in arr:  # O(n) search
        return True

# Fast: O(n)
seen = set()
for num in arr:
    if target - num in seen:  # O(1) lookup
        return True
    seen.add(num)
```

### Avoid Nested Loops
```python
# Slow: O(n²)
result = []
for i in arr1:
    for j in arr2:
        if i == j:
            result.append(i)

# Fast: O(n)
set1 = set(arr1)
result = [x for x in arr2 if x in set1]
```

### Use Built-ins
Python's built-in functions are optimized in C:
- `sorted()` is O(n log n)
- `min()`, `max()`, `sum()` are O(n)
- `in` for sets/dicts is O(1) average

---

## 🧪 Practice Problems by Complexity

- **O(1):** Hash lookup, array access
- **O(log n):** Binary search (#24)
- **O(n):** Two sum (#21), palindrome (#3)
- **O(n log n):** Merge intervals (#23)
- **O(n²):** Matrix transpose (#9)

---

## 📚 Resources

- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Visualizing Algorithms](https://visualgo.net/)

