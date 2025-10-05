def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        for num in nums:
            result = []
            if num - 1 not in nums:
                start = num
                result = [num]
                numsX = sorted(nums)
                for num in numsX:
                    if num == result[-1] + 1:
                        result.append(num)
                max_len = max(max_len, len(result))
        return max_len


# Time Complexity: O(n log n) due to the sorting step.
# Space Complexity: O(n) in the worst case when all elements are part of the longest consecutive sequence.


# The function iterates through each number in the input list and checks if it is the start of a potential consecutive sequence (i.e., if the previous number is not in the list).
# If it is the start, it initializes a result list with that number and sorts the input list to facilitate finding consecutive numbers.
# It then iterates through the sorted list, appending numbers to the result list if they are consecutive (i.e., if they are exactly one greater than the last number in the result list).
# After building the consecutive sequence, it updates the maximum length found so far. 
# Finally, it returns the maximum length of consecutive numbers found.
# The time complexity is O(n log n) because of the sorting step, which dominates the overall complexity.
# The space complexity is O(n) in the worst case when all elements are part of the longest consecutive sequence, as they would all be stored in the result list.

