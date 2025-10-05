def hasDuplicate(self, nums: List[int]) -> bool:
    numsDict = {}
    for num in nums:
        if num not in numsDict:
            numsDict[num] = 1
        else:
            numsDict[num] += 1
            if numsDict[num] > 1:
                return True
    return False


# Time Complexity: O(n) where n is the number of elements in the input list
# Space Complexity: O(n) for storing the elements in the dictionary

# We initialize an empty dictionary `numsDict` to keep track of the occurrences of each number in the input list `nums`.
# We iterate through each number `num` in the input list `nums`. For each number, we check if it is already present in the dictionary `numsDict`.
# If the number is not present in the dictionary, we add it with a count of 1.
# If the number is already present in the dictionary, we increment its count by 1.  
# If the count of any number exceeds 1, we immediately return True, indicating that a duplicate has been found.
# If we finish iterating through the entire list without finding any duplicates, we return False.

# The time complexity is O(n) because we may need to check each element in the input list once. 
# The space complexity is also O(n) in the worst case, where all elements are unique and need to be stored in the dictionary.