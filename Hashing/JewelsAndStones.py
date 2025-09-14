def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stonesDict = {}
        for jewel in stones:
            if jewel not in stonesDict and jewel in jewels:
                stonesDict[jewel] = 1
            elif jewel in jewels:
                stonesDict[jewel] += 1
        
        count = 0
        for value in stonesDict.values():
            count += value
        return count


# Time Complexity : O(n) where n is the length of the stones string
# Space Complexity : O(n) since we are using a hashmap to store the stones


# Explanation: We create a hashmap to store the stones that are also jewels.
# We then iterate through the stones string and add each stone to the hashmap if it is also a jewel.
# Finally, we iterate through the hashmap and sum the values to get the total number of jewels in the stones string.
# We return the count at the end.