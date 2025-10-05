def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numsDict:
                return [numsDict[complement], i]
            numsDict[nums[i]] = i

# Time complexity: O(n)
# Space complexity: O(n)

# Explanation:
# The function uses a dictionary to keep track of the number which is needed to reach the target sum for each number in the list.
# It keeps track of the index of each number in the dictionary and when the complement is found, it returns the indicies of the two numbers.


