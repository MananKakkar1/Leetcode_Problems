# LeetCode Data Structures & Algorithms Notes

## Table of Contents
- [LeetCode Data Structures \& Algorithms Notes](#leetcode-data-structures--algorithms-notes)
  - [Table of Contents](#table-of-contents)
  - [Section 1: Arrays and Strings](#section-1-arrays-and-strings)
    - [Time Complexity Reference](#time-complexity-reference)
    - [Part 1: Two Pointers](#part-1-two-pointers)
    - [Part 2: Sliding Window](#part-2-sliding-window)
    - [Part 3: Prefix Sum](#part-3-prefix-sum)
  - [Section 2: Hash Maps \& Sets (Hashing)](#section-2-hash-maps--sets-hashing)
    - [Hashing](#hashing)
    - [Hash Map (dictionary)](#hash-map-dictionary)

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

    # process remaining left or right movements for variable i or j respectively
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

---

### Part 3: Prefix Sum

**Prefix Sum** creates an array `prefix` where `prefix[i]` is the sum of elements up to index `i` (inclusive). `prefix[i-1]` is the sum of numbers before `i`. This lets you compute any subarray sum in **O(1)**.



**Psuedocode:**

```cpp
// Given an array nums,
prefix = [nums[0]]
for (int i = 1; i < nums.length; i++) {
    prefix.append(nums[i] + prefix[prefix.length - 1])
}
```

**Common pitfalls**
- Off-by-one when using 0-indexed arrays.
- Resetting prefix when multiple test cases are processed.
- Mixing inclusive/exclusive boundaries when computing ranges.


## Section 2: Hash Maps & Sets (Hashing)

### Hashing
A **hash function** turns a key into an integer in `[0, M-1]` (deterministic). That index picks a bucket in an internal array.

Arrays give O(1) access for integer indices. Hashing lets me treat *any* key like an index → enabling hash maps/dictionaries.

---

### Hash Map (dictionary)
Stores **key → value** pairs. Keys should be **immutable**; values can be anything.

**Average-case operations:**
- Insert / Update / Delete / Contains: **O(1)**
- Get value by key: **O(1)**
- Iterate over items: **O(n)** (order not guaranteed; language-dependent)

**Nuances:**
- Worst case with many collisions → **O(n)**, but good hashes/load factors keep average O(1).
- Resizing a table is expensive (rehash), so there’s overhead compared to small plain arrays.

**Common Types of Patterns in Questions:**
- Counting & frequency tables
- Two-Sum style complements
- Checking for existence
