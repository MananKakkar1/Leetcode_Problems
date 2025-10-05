def maxProfit(self, prices: List[int]) -> int:
        left = 0
        res = 0
        for right in range(len(prices)):
            if left == right:
                continue
            if prices[left] >= prices[right]:
                left = right
            else:
                res = max(res, prices[right] - prices[left])
        return res



# Time Complexity: O(n)
# Space Complexity: O(1)    

# The function uses a two-pointer approach to find the maximum profit that can be achieved by buying and selling a stock given its prices over time.
# It initializes a left pointer to track the day to buy the stock and iterates through the prices with a right pointer to track the day to sell the stock.
# If the price at the left pointer is greater than or equal to the price at the right pointer, it updates the left pointer to the right pointer, indicating a new potential buying day.
# If the price at the left pointer is less than the price at the right pointer, it calculates the potential profit and updates the maximum profit found so far.
# The time complexity is O(n) because each price in the list is processed at most once.
# The space complexity is O(1) because no additional space is used that scales with the input size.