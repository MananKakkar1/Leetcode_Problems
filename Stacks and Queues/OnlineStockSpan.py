class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            span += prev_span
        self.stack.append((price, span))
        return span
    

# Time Complexity: O(1) on average for next() (amortized)
# Space Complexity: O(n) where n is the number of calls to next()

# Explanation:
# We maintain a stack that stores pairs of (price, span).
# For each new price, we initialize its span to 1.
# We then pop from the stack while the top price is less than or equal to the current price, adding the popped spans to the current span.
# Finally, we push the current price and its computed span onto the stack and return the span.