# Data Structures & Algorithms Patterns

Quick reference guide for common patterns used in the practice problems.

---

## 🔍 Search Patterns

### Linear Search
- **Time:** O(n)
- **Space:** O(1)
- **Use:** Unsorted data, small datasets

### Binary Search
- **Time:** O(log n)
- **Space:** O(1) iterative, O(log n) recursive
- **Use:** Sorted arrays
- **Problems:** #24

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

---

## 🔢 Two Pointers

### Pattern
- Use two pointers to traverse array from both ends or same direction
- **Time:** Usually O(n)
- **Space:** O(1)

### Applications
- Finding pairs with target sum
- Removing duplicates
- Container with most water
- **Problems:** #21, #29

```python
# Two sum in sorted array
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None
```

---

## 🪟 Sliding Window

### Pattern
- Maintain a window that slides through array
- **Time:** O(n)
- **Space:** O(k) where k is window size

### Applications
- Maximum/minimum subarray
- Longest substring without repeating characters
- **Problems:** #29

```python
# Longest substring without repeating chars
def longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

---

## 📚 Stack & Queue

### Stack (LIFO)
- **Use:** Matching brackets, undo operations, DFS
- **Problems:** #22

```python
def valid_parentheses(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs:
            stack.append(char)
        elif not stack or pairs[stack.pop()] != char:
            return False
    
    return len(stack) == 0
```

### Queue (FIFO)
- **Use:** BFS, task scheduling
- **Problems:** #28, #44

---

## 🗺️ Hash Maps/Sets

### Pattern
- Trade space for time
- **Time:** O(1) average for lookups
- **Space:** O(n)

### Applications
- Frequency counting
- Fast lookups
- Caching
- **Problems:** #4, #7, #21, #27

```python
from collections import Counter

def frequency_counter(s):
    return Counter(s)  # or dict
```

---

## 🌳 Trees & Graphs

### DFS (Depth-First Search)
- **Implementation:** Recursion or stack
- **Space:** O(h) where h is height

### BFS (Breadth-First Search)
- **Implementation:** Queue
- **Space:** O(w) where w is max width
- **Problems:** #28

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        # Process node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

---

## 💾 Dynamic Programming

### Pattern
- Break problem into overlapping subproblems
- Store solutions to avoid recomputation
- **Bottom-up (Tabulation)** or **Top-down (Memoization)**

### Applications
- Fibonacci, path counting, knapsack
- **Problems:** #30, #45

```python
# Matrix paths - bottom-up
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]
```

---

## 🔄 Sorting & Merging

### Common Sorts
- **Quick Sort:** O(n log n) average, O(n²) worst
- **Merge Sort:** O(n log n) guaranteed
- **Heap Sort:** O(n log n), in-place

### Merge Pattern
- Used in merge intervals, merge sorted arrays
- **Problems:** #23

```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    
    return merged
```

---

## 🎯 Greedy Algorithms

### Pattern
- Make locally optimal choice at each step
- Hope it leads to global optimum

### Applications
- Activity selection, Huffman coding
- Works when problem has greedy-choice property

---

## 🔗 Linked Lists

### Techniques
- **Dummy head:** Simplify edge cases
- **Two pointers:** Fast/slow for cycle detection
- **Reverse:** Iterative or recursive

**Problems:** #25

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev
```

---

## 📊 Heaps

### Pattern
- Priority queue implementation
- **Time:** O(log n) insert/delete, O(1) peek
- **Use:** K-th largest/smallest, merge K sorted lists

**Problems:** #27

```python
import heapq

def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
```

---

## 🧮 Bit Manipulation

### Common Operations
```python
# Check if bit is set
(n & (1 << i)) != 0

# Set bit
n | (1 << i)

# Clear bit
n & ~(1 << i)

# Toggle bit
n ^ (1 << i)
```

---

## ⏱️ Time Complexity Cheatsheet

| Complexity | Name | Example |
|------------|------|---------|
| O(1) | Constant | Hash lookup, array access |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single loop |
| O(n log n) | Linearithmic | Merge sort, heap sort |
| O(n²) | Quadratic | Nested loops |
| O(2ⁿ) | Exponential | Recursive Fibonacci |
| O(n!) | Factorial | Permutations |

---

## 💡 Problem-Solving Strategy

1. **Understand** the problem (examples, constraints)
2. **Plan** the approach (brute force first)
3. **Optimize** (identify bottlenecks)
4. **Code** the solution
5. **Test** (edge cases, performance)
6. **Refactor** (clean, readable)

---

## 📝 Notes

Add your own patterns and insights as you work through the problems!

