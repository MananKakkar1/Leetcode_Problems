class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]



# Time Complexity: O(1) for all operations (push, pop, top, getMin)
# Space Complexity: O(n) where n is the number of elements in the stack


# We maintain two stacks: `stack` for the actual stack elements and `minStack` to keep track of the minimum elements.
# When pushing a new value, we add it to `stack` and also update `minStack` with the minimum value between the new value and the current minimum (top of `minStack`).
# When popping, we remove the top elements from both `stack` and `minStack`.
# The `top` method returns the top element of `stack`, and `getMin` returns the top element of `minStack`, which is always the minimum value in the stack.
# This design ensures that all operations are performed in constant time, O(1), and the space complexity is linear, O(n), due to the storage of elements in both stacks.