# LeetCode DSA Course Notes

> Converted from your notes and expanded into a single README-friendly file (with images reproduced as Markdown).


## Table of Contents
- [Section 1: Arrays and Strings](#section-1-arrays-and-strings)
  - [Time Complexity Reference](#time-complexity-reference)
  - [Part 1: Two Pointers](#part-1-two-pointers)
  - [Part 2: Sliding Window](#part-2-sliding-window)
  - [Part 3: Prefix Sum](#part-3-prefix-sum)

## Section 1: Arrays and Strings

Appending to the end of a list gives **amortized O(1)** complexity.


### Time Complexity Reference

| Operation                  | Array/List | String (Immutable) |
|----------------------------|------------|---------------------|
| Appending to end           | *O(1)      | O(n)               |
| Popping from end           | O(1)       | O(n)               |
| Insertion, not from end    | O(n)       | O(n)               |
| Deletion, not from end     | O(n)       | O(n)               |
| Modifying an element       | O(1)       | O(n)               |
| Random access              | O(1)       | O(1)               |
| Checking if element exists | O(n)       | O(n)               |

---

### Part 1: Two Pointers

The **two pointers** algorithm is used to solve array and string problems.

There are two ways of using it:


- **Case 1: Single input** — Start each pointer from the edges of the input and move them toward each other until they meet.

- **Case 2: Two inputs** — Move pointers along both inputs simultaneously until all elements have been checked.



**When to use**
- Pair/sum comparisons on sorted arrays
- Palindrome checks / reverse-in-place
- Merging or deduping two sorted inputs
- Partitioning around a pivot

**Template (Python)**
```python
def two_pointers(arr):
    i, j = 0, len(arr) - 1
    while i <= j:
        # process arr[i], arr[j]
        if should_move_left(i, j, arr):
            i += 1
        elif should_move_right(i, j, arr):
            j -= 1
        else:
            i += 1
            j -= 1
```

**Template (C++)**
```cpp
int i = 0, j = (int)arr.size() - 1;
while (i <= j) {
    // process arr[i], arr[j]
    if (should_move_left(i, j, arr))      ++i;
    else if (should_move_right(i, j, arr)) --j;
    else { ++i; --j; }
}
```


---

### Part 2: Sliding Window

Use **sliding window** when problems describe **subarrays being “valid”** and ask you to **find them**.



**How to use**
1. Let `left` and `right` be the bounds of the window. Initialize `left = right = 0` (consider the first element).
2. Expand by incrementing `right` to include the new element.
3. If the window becomes invalid after adding, increment `left` until valid again.
4. Many tasks ask for the **best valid subarray**, the **number of valid subarrays**, or a **fixed-length** window.

**Window Length**
```
right - left + 1
```

**Why it’s efficient**
Sliding window reduces a typical O(n^2) scan for subarrays to O(n) by moving each pointer at most n steps.

**Template: variable-size window (Python)**
```python
def sliding_window(arr):
    left = 0
    best = 0
    state = {}  # counts, sum, distinct, etc.
    for right, x in enumerate(arr):
        # include x
        # update 'state' to reflect adding arr[right]
        while not is_valid(state):
            # remove arr[left]
            left += 1
        best = max(best, right - left + 1)  # or update answer differently
    return best
```

**Template: fixed-size window (Python)**
```python
def fixed_k_max_sum(arr, k):
    window_sum = sum(arr[:k])
    best = window_sum
    for right in range(k, len(arr)):
        window_sum += arr[right] - arr[right - k]
        best = max(best, window_sum)
    return best  # window length is always k
```


---

### Part 3: Prefix Sum

**Prefix Sum** creates an array `prefix` where `prefix[i]` is the sum of elements up to index `i` (inclusive). `prefix[i-1]` is the sum of numbers before `i`. This lets you compute any subarray sum in **O(1)**.



**Example (from image, reproduced)**

```cpp
// Given an array nums,
prefix = [nums[0]]
for (int i = 1; i < nums.length; i++) {
    prefix.append(nums[i] + prefix[prefix.length - 1])
}
```

**0-indexed subarray sum**
For subarray sum of `nums[l..r]` (inclusive), use:
```
sum = prefix[r] - (l > 0 ? prefix[l - 1] : 0)
```

**Template (Python)**
```python
def build_prefix(nums):
    pref = [0] * len(nums)
    pref[0] = nums[0]
    for i in range(1, len(nums)):
        pref[i] = pref[i-1] + nums[i]
    return pref
```

**Common pitfalls**
- Off-by-one when using 0-indexed arrays.
- Resetting prefix when multiple test cases are processed.
- Mixing inclusive/exclusive boundaries when computing ranges.
