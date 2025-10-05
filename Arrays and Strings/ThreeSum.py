def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res



# Time Complexity: O(n^2) where n is the number of elements in nums.
# Space Complexity: O(n) for the output list storing the triplets.

# The function first sorts the input list to facilitate the two-pointer technique.
# It then iterates through each element, treating it as a potential first element of a triplet.
# For each element, it uses two pointers (left and right) to find pairs that sum to the negative of the current element.
# If the sum of the triplet is greater than zero, it moves the right pointer left to decrease the sum.
# If the sum is less than zero, it moves the left pointer right to increase the sum.
# If a triplet is found that sums to zero, it adds it to the result list and moves both pointers inward, skipping over duplicate values to avoid repeating triplets.
# The time complexity is O(n^2) because for each element, we potentially traverse the rest of the list with two pointers.
# The space complexity is O(n) due to the output list that stores the unique triplets.