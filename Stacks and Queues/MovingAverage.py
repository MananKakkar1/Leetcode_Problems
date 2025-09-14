class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = []

    def next(self, val: int) -> float:
        self.window.append(val)
        # print(self.window, len(self.window) > self.size)
        if len(self.window) > self.size:
            self.window.pop(0)
        # print(self.window, val)
        return sum(self.window) / len(self.window)
    

# Time Complexity: O(1) for next() on average (amortized due to pop(0))
# Space Complexity: O(n) where n is the size of the moving window

# Explanation:
# We maintain a list `window` to store the last 'size' elements.
# When a new value is added via `next()`, we append it to the list.
# If the list exceeds the specified size, we remove the oldest element (the first one).
# We then compute the average by dividing the sum of the elements in the list by its length.
# This approach ensures that we always have the most recent 'size' elements for the moving average calculation.