def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            counts = [0]*26
            for char in s:
                counts[ord(char) - ord('a')] += 1
            groups[tuple(counts)].append(s)
        return list(groups.values())



# Time Complexity: O(n * k) where n is the number of strings and k is the maximum length of a string.   
# Space Complexity: O(n * k) in the worst case when all strings are different.

# The function uses a defaultdict to group anagrams together. 
# For each string, it creates a count of each character (assuming only lowercase letters a-z) and uses this count as a key in the dictionary. 
# The string is then appended to the list corresponding to that key.
# Finally, it returns the values of the dictionary as a list of lists.
# This approach ensures that all anagrams are grouped together based on their character counts.
# The time complexity is O(n * k) because we iterate through each of the n strings and for each string, we count the characters which takes O(k) time.
# The space complexity is O(n * k) in the worst case when all strings are different, as we store each string in the dictionary.