def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n
        prefix = 1
        suffix = 1
        for i in range(n):
            out[i] = prefix
            prefix *= nums[i]
        for i in range(n-1, -1, -1):
            out[i] *= suffix
            suffix *= nums[i]
        return out



# Time Complexity: O(n)
# Space Complexity: O(n)

# The function initializes an output list with 1s, which will eventually hold the product of all elements except the current one.
# It then calculates the prefix product for each element in a single pass from left to right, storing the result in the output list.
# Next, it calculates the suffix product in a single pass from right to left, multiplying it with the existing values in the output list.
# This way, each element in the output list contains the product of all elements to its left and all elements to its right.
# The time complexity is O(n) because we make two passes through the list of numbers.
# The space complexity is O(n) because we use an output list of the same size as the input list.