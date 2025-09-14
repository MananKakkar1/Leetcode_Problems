def missingNumber(self, nums: List[int]) -> int:
        minNum = 0
        maxNum = len(nums)
        
        rangeDict = {}
        for i in range(minNum, maxNum + 1):
            rangeDict[i] = 0
            
        for num in nums:
            rangeDict[num] += 1
        
        for key, value in rangeDict.items():
            if value == 0:
                return key
            

# Time Complexity : O(n) where n is the length of the nums array
# Space Complexity : O(n) since we are using a hashmap to store the range of numbers

# Explanation: We create a hashmap to store the range of numbers from 0 to n. 
# We then iterate through the nums array and increment the count of each number in the hashmap.
# Finally, we iterate through the hashmap and return the key with a value of 0, which is the missing number.
