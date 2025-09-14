def findMaxLength(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[i - 1] + nums[i])
        
        first_index = {0: -1}
        max_len = 0

        for i in range(len(prefixSum)):
            diff = 2 * prefixSum[i] - (i + 1)

            if diff in first_index:
                length = i - first_index[diff]
                if length > max_len:
                    max_len = length
            else:
                first_index[diff] = i

        return max_len


# Time Complexity : O(n) where n is the length of the nums array
# Space Complexity : O(n) since we are using a hashmap to store the prefix sums


# Explanation: We create a prefix sum array where each element at index i is the sum of all elements from index 0 to i in the nums array.
# We then create a hashmap to store the first occurrence of each prefix sum.
# We iterate through the prefix sum array and calculate the difference between twice the prefix sum and the current index + 1.
# If this difference has been seen before, we calculate the length of the subarray and update the max_len if it's greater than the current max_len.
# If the difference has not been seen before, we store the current index as the first occurrence of this difference.
# Finally, we return the max_len at the end.