def countElements(self, arr: List[int]) -> int:
        countDict = {}
        count = 0
        for item in arr:
            if item not in countDict:
                countDict[item] = 1
            else:
                countDict[item] += 1
        
        for key, value in countDict.items():
            if key + 1 in countDict:
                count += value
        
        return count


# Time Complexity : O(n) where n is the length of the arr array
# Space Complexity : O(n) since we are using a hashmap to store the elements in the arr array

# Explanation: We create a hashmap to store the elements in the arr array. 
# We then iterate through the arr array and add each element to the hashmap.
# Finally, we iterate through the hashmap and check if the key + 1 exists in the hashmap.
# If it does, we increment the count by the value of the key in the hashmap.
# We return the count at the end.