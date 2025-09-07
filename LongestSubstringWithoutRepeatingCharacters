def lengthOfLongestSubstring(self, s: str) -> int:
    seen = {}
    maxLen = 0
    start = 0
    for i in range(len(s)):
        char = s[i]
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = i
        currLen = i - start + 1
        maxLen = max(maxLen, currLen)
    return maxLen
        
        
# Time complexity: O(n) where n is the length of the string.
# Space complexity: O(min(m, n)) where m is the size of the character set

# Explanation:
# The function uses a dictionary to keep track of the last seen index of each character in the string.
# It maintains a sliding window defined by the start index and the current index.
# When a repeating character is found within the current window, the start index is updated to the index after the last occurrence of that character.
# The length of the current substring is calculated as the difference between the current index and the start index plus one.
# The maximum length of the substring without repeating characters is updated accordingly.

