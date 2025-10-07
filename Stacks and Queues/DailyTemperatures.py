def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = i - stack_index
            stack.append((temp, i))
        return result



# Time Complexity: O(n), where n is the number of temperature readings.
# Space Complexity: O(n), in the worst case when temperatures are in decreasing order.

# The function calculates, for each day, how many days one has to wait until a warmer temperature occurs.
# It uses a monotonic decreasing stack to keep track of previous temperatures that haven’t yet found a warmer day.
# For each temperature in the list:
#   - While the current temperature is greater than the temperature at the top of the stack,
#     it pops from the stack and updates the result for that popped index with the difference in days.
#   - The current temperature (with its index) is then pushed onto the stack.
# After processing all temperatures, any indices still in the stack have no warmer future day, so they remain 0 in the result list.
# The time complexity is O(n) because each temperature is pushed and popped from the stack at most once.
# The space complexity is O(n) in the worst case when the temperatures are strictly decreasing,
# as all of them would remain in the stack.