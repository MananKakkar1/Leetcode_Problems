def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        maxArray = []
        curr = []
        for right in range(len(nums)):
            curr = nums[left:right+1]
            if right - left + 1 >= k:
                if len(curr) == k:
                    maxArray.append(max(curr))
                left += 1
        return maxArray


# Time Complexity: O(n * k)
# Space Complexity: O(n - k + 1)

# The function uses a sliding window approach to find the maximum value in each subarray of size k in the input list.
# It initializes a left pointer to track the start of the window and iterates through the list with a right pointer to expand the window.
# For each position of the right pointer, it checks if the current window size (right - left + 1) is at least k.
# If the window size is equal to k, it calculates the maximum value in the current window and appends it to the result list (maxArray).
# The left pointer is then incremented to slide the window forward.
# The time complexity is O(n * k) because for each of the n elements in the list, the algorithm may need to compute the maximum of a subarray of size k.
# The space complexity is O(n - k + 1) because the output list (maxArray) will contain (n - k + 1) maximum values, where n is the length of the input list.
# Note: This implementation can be optimized to O(n) time complexity using a deque to maintain the indices of the maximum elements in the current window.
# def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         output = []
#         q = deque()  # index
#         l = r = 0
#         while r < len(nums):
#             while q and nums[q[-1]] < nums[r]:
#                 q.pop()
#             q.append(r)
#             if l > q[0]:
#                 q.popleft()
#             if (r + 1) >= k:
#                 output.append(nums[q[0]])
#                 l += 1
#             r += 1
#         return output
# Time Complexity: O(n)
# Space Complexity: O(k)
# The optimized function uses a deque to maintain the indices of the maximum elements in the current sliding window.
# It ensures that the deque only contains indices of elements that are within the current window and removes indices of elements that are less than the current element being processed.
# This allows the function to efficiently retrieve the maximum element in O(1) time for each window position, resulting in an overall time complexity of O(n).