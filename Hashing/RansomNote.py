def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineDict = {}
        for s in magazine:
            if s not in magazineDict:
                magazineDict[s] = 1
            else:
                magazineDict[s] += 1
        
        for char in ransomNote:
            if char not in magazineDict or magazineDict[char] < 1:
                return False
            else:
                magazineDict[char] -= 1
        return True


# Time Complexity : O(m + n) where m is the length of the ransomNote and n is the length of the magazine
# Space Complexity : O(1) since the size of the hashmap will be at max 26 (number of letters in the English alphabet)

# Explanation: We create a hashmap to store the characters in the magazine.
# We then iterate through the magazine and add each character to the hashmap.
# We use the get method of the dictionary to return 0 if the character is not found in the hashmap.
# Finally, we iterate through the ransomNote and check if each character is in the hashmap and if its count is greater than 0.
# If it is, we decrement the count of that character in the hashmap.
# If we find a character that is not in the hashmap or its count is 0, we return False.
# If we successfully iterate through the ransomNote, we return True.