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
    - [Counting (frequency)](#counting-frequency)
    - [Exact constraints with prefix sums + counts](#exact-constraints-with-prefix-sums--counts)
  - [Section 3: Linked Lists](#section-3-linked-lists)
    - [Basics](#basics)
    - [Advantages vs Arrays](#advantages-vs-arrays)
    - [Mechanics](#mechanics)
    - [Traversal](#traversal)
    - [Singly Linked List: Insert/Delete](#singly-linked-list-insertdelete)
    - [Doubly Linked List](#doubly-linked-list)
    - [Sentinel Nodes](#sentinel-nodes)
    - [Dummy Pointer](#dummy-pointer)
    - [Complexity Reference](#complexity-reference)
  - [Section 3: Part 1: Slow and Fast Pointers](#section-3-part-1-slow-and-fast-pointers)
  - [Section 3: Part 2: Reversing a Linked List](#section-3-part-2-reversing-a-linked-list)

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

### Counting (frequency)

Use a hash map to track **frequencies** (`key -> count`). This pairs well with sliding window when the constraint involves **multiple distinct elements**.

- Maintain `counts[...] += 1` when expanding the window.
- When shrinking, decrement and **delete** keys when the count hits 0.
- Amortized **O(1)** per step ⇒ overall **O(n)**.

### Exact constraints with prefix sums + counts

For “**number of subarrays with sum exactly = k**” (or “exactly k odds”):
- Keep a running `curr` (prefix).
- Keep `counts[prefix]` with **`counts[0] = 1`** to account for the empty prefix.
- At each index: `ans += counts[curr - k]`, then do `counts[curr] += 1`.

This mirrors Two-Sum: fix `curr`, look up `curr - k`.

**Common Types of Patterns in Questions:**
- Counting & frequency tables
- Two-Sum style complements
- Checking for existence


## Section 3: Linked Lists
### Basics
- A linked list stores elements as **nodes**. Each node keeps a value and a pointer/reference to the next node (`next`).
- The **head** is the first node and is the only guaranteed way to reach the entire list. Keep a reference to it.
- The list ends at a node whose `next` is `null` (or equivalent).

### Advantages vs Arrays
- **Insert/Delete at a known position** is **O(1)** *if you already have the predecessor node*. Otherwise, it’s **O(n)** to walk there.
- **No random access**: accessing the element at index `i` is **O(n)** from the head.
- **No resizing cost**: lists grow/shrink by linking/unlinking nodes, but each node has **extra pointer overhead** (and worse cache locality than arrays).

### Mechanics
- **Reference assignment** points to the same node. Reassigning `head = head.next` does not change other references pointing at the old head.
- **Chaining** like `head.next.next` means: go to the node after `head`, then take **its** `next`.
- **Order of rewiring matters** when inserting/deleting to avoid “losing” part of the list.

### Traversal
- Move a cursor from `head` forward one node at a time until reaching the end.
- Can be written iteratively or recursively (watch stack depth for very long lists).

### Singly Linked List: Insert/Delete
- **Insert after `prev`**: point the new node’s `next` to `prev.next`, then point `prev.next` to the new node. This is **O(1)** if `prev` is known.
- **Delete after `prev`**: point `prev.next` to `prev.next.next`. This is **O(1)** if `prev` is known.
- Without a direct pointer to `prev`, you must **walk from head** to find it → **O(n)**.

### Doubly Linked List
- Each node has both `prev` and `next` pointers, allowing **bidirectional** iteration.
- Insert/delete requires **updating both directions** (adjust `prev` on the successor and `next` on the predecessor).
- Often used when frequent front/back operations or backward traversal are needed.

### Sentinel Nodes
- Use **dummy head** (and **dummy tail** for doubly lists) to simplify edge cases:
  - Uniform insert/delete at front/back with fewer `null` checks.
  - Cleaner code for operations on empty or single-element lists.
- The real list starts at `dummy_head.next` (and ends at `dummy_tail.prev` in doubly lists).

### Dummy Pointer
- Keep `head` untouched and walk with a **separate cursor** (dummy pointer) to avoid losing access to the list’s start.

### Complexity Reference
| Task                                  | Time   | Space |
|---------------------------------------|--------|-------|
| Access by index `i`                   | O(n)   | O(1)  |
| Search by value                       | O(n)   | O(1)  |
| Insert/delete (with predecessor)      | O(1)   | O(1)  |
| Insert/delete by index (no pointer)   | O(n)   | O(1)  |
| Reverse list                          | O(n)   | O(1)  |
| Merge two sorted lists                | O(n+m) | O(1)  |

## Section 3: Part 1: Slow and Fast Pointers

**Idea**  
An implementation of two pointers where the pointers don’t move in lockstep. Commonly, the **fast** pointer advances two nodes per step while the **slow** pointer advances one (but any speed/offset difference works). Sometimes the pointers **start at different positions** instead of moving at different speeds.

**When to use**
- Find the **middle** of a list without knowing its length.
- **Detect** if a cycle exists and **locate** the cycle’s start.
- Maintain a **fixed gap** between two pointers (variant: unequal starts rather than unequal speeds).

```python
slow, fast = head, head
while fast and fast.next:
    # do any per-iteration work here (e.g., check meeting)
    slow = slow.next            # +1 step
    fast = fast.next.next       # +2 steps
# if loop ends by exhaustion: fast hit the end (no cycle)
# slow typically lands at middle of list
```

## Section 3: Part 2: Reversing a Linked List
**Idea**  
Reverse pointers in-place using three references: `prev`, `curr`, `next_node`. Flip `curr.next` to point at `prev`, then advance.

**Steps**
1. `next_node = curr.next` — don’t lose the remainder of the list.
2. `curr.next = prev` — flip the arrow.
3. `prev = curr` — move `prev` forward.
4. `curr = next_node` — move `curr` forward.
5. Loop until `curr` is `None`; **return `prev`** (new head).

```python
def reverse_list(head):
    prev, curr = None, head
    while curr:
        next_node = curr.next   # save next
        curr.next = prev        # reverse pointer
        prev = curr             # advance prev
        curr = next_node        # advance curr
    return prev                 # new head
```

**Why save ```next_node```?**

After ```curr.next = prev```, the original node would be unreachable without storing it first.

**Complexity**
- Time: O(n)
- Space: O(1)
