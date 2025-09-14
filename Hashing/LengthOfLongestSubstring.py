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


# Time Complexity : O(n) where n is the length of the string s
# Space Complexity : O(min(m, n)) where m is the size of the charset/al

# Explanation: We use a sliding window approach to keep track of the longest substring without repeating characters.
# We use a hashmap to store the characters in the current window and their indices.
# We iterate through the string and for each character, we check if it is already in the hashmap and if its index is greater than or equal to the start of the current window.
# If it is, we update the start of the window to be the index of the character + 1.
# We then update the index of the character in the hashmap and calculate the current length of the window.
# We update the maximum length if the current length is greater than the maximum length.
# Finally, we return the maximum length at the end. 