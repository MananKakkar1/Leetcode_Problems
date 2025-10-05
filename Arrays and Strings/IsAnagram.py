def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sDict = {}
        tDict = {}
        for char in s:
            if char not in sDict:
                sDict.setdefault(char, 1)
            else:
                sDict[char] += 1
        for char in t:
            if char not in tDict:
                tDict.setdefault(char, 1)
            else:
                tDict[char] += 1
        for key, value in sDict.items():
            if key not in tDict:
                return False
            if tDict[key] != sDict[key]:
                return False
        return True


# Time Complexity: O(n)
# Space Complexity: O(n)

# Firstly, we check if the lengths of the two strings are equal. If not, they cannot be anagrams, so we return False.
# We then create two dictionaries to count the occurrences of each character in both strings.
# We iterate through each character in the first string, updating its count in the first dictionary.
# We do the same for the second string and its corresponding dictionary.
# Finally, we compare the two dictionaries. If they have the same keys with the same counts, we return True; otherwise, we return False.
# This approach ensures that we accurately count and compare the characters in both strings to determine if they are anagrams.
# This solution has a time complexity of O(n) and a space complexity of O(n), where n is the length of the strings.
