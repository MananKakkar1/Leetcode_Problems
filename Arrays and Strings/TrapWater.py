def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        l, r = 0, n - 1
        left_max, right_max = height[l], height[r]
        res = 0
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]
        return res


# Time Complexity: O(n)
# Space Complexity: O(1)

# The function uses a two-pointer approach to calculate the amount of water that can be trapped between the bars represented by the heights in the input list.
# It initializes two pointers, one at the beginning (left) and one at the end (right) of the list, along with variables to keep track of the maximum heights encountered from both ends (left_max and right_max).
# The algorithm iterates until the two pointers meet, updating the left and right maximum heights and calculating the trapped water at each step.
# If the left maximum height is less than the right maximum height, it moves the left pointer to the right, updates the left maximum height, and adds the difference between the left maximum height and the current height to the result.
# If the right maximum height is less than or equal to the left maximum height, it moves the right pointer to the left, updates the right maximum height, and adds the difference between the right maximum height and the current height to the result.
# The time complexity is O(n) because each element in the list is processed at most once.
# The space complexity is O(1) because no additional space is used that scales with the input size.