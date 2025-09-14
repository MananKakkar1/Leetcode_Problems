def largestUniqueNumber(self, nums: List[int]) -> int:
        numsDict = {}
        maxInt = -9999999999
        for num in nums:
            if num not in numsDict:
                numsDict[num] = 1
            else:
                numsDict[num] += 1
            
        for key, value in numsDict.items():
            if value == 1:
                maxInt = max(maxInt, key)
        
        return maxInt if maxInt != -9999999999 else -1


# Time Complexity : O(n) where n is the length of the nums array
# Space Complexity : O(n) since we are using a hashmap to store the elements in the

# Explanation: We create a hashmap to store the elements in the nums array.
# We then iterate through the nums array and add each element to the hashmap.
# Finally, we iterate through the hashmap and check if the value of each key is 1.
# If it is, we update the maxInt variable to be the maximum of the current maxInt and the key.
# We return maxInt at the end, or -1 if no unique number was found.
