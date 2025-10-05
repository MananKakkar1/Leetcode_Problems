def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_volume = 0
        while left < right:
            volume = (right - left) * min(heights[left], heights[right])
            max_volume = max(max_volume, volume)
            if min(heights[left], heights[right]) == heights[left]:
                left += 1
            elif min(heights[left], heights[right]) == heights[right]:
                right -= 1
        return max_volume



# Time Complexity: O(n)
# Space Complexity: O(1)

# The function uses a two-pointer approach to find the maximum area of water that can be contained between two lines represented by the heights in the input list.
# It initializes two pointers, one at the beginning (left) and one at the end (right) of the list.
# It calculates the area formed between the lines at these two pointers and updates the maximum area found so far.
# The pointer corresponding to the shorter line is then moved inward, as moving the taller line would not increase the area.
# This process continues until the two pointers meet.
# The time complexity is O(n) because each element in the list is processed at most once.
# The space complexity is O(1) because no additional space is used that scales with the input size.
