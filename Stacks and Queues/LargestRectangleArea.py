def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea



# Time Complexity: O(n), where n is the number of bars in the histogram.
# Space Complexity: O(n), since the stack can hold up to n bars in the worst case.
#
# This function calculates the largest rectangular area possible in a histogram.
# It uses a monotonic stack to efficiently keep track of bars in increasing order of height.
# As we iterate through each bar, we maintain the start index where the current height can extend back.
# When we encounter a bar that is shorter than the one on top of the stack, it means the rectangle
# formed by the taller bar on the stack has ended. We pop it from the stack and calculate its area
# using the width between the current index and the popped bar’s start index.
# After processing all bars, we go through the remaining stack to calculate areas
# for bars that extend to the end of the histogram.
# The result is the maximum area found among all such rectangles.