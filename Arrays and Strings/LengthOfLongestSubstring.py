def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 1
        maxLen = 1
        if s == "":
            return 0
        while right < len(s):
            curr = s[left:right+1]
            if not len(curr) != len(set(curr)):
                maxLen = max(maxLen, len(curr))
                right += 1
            else:
                left += 1
        return maxLen



# Time Complexity: O(n)
# Space Complexity: O(n)

# The function uses a sliding window approach to find the length of the longest substring without repeating characters.
# It initializes two pointers, left and right, to represent the current window of characters being considered.
# The right pointer expands the window by moving to the right, while the left pointer contracts the window by moving to the right when a duplicate character is found.
# The current substring is checked for duplicates by comparing its length to the length of the set of its characters (which removes duplicates).
# If the lengths are equal, it means there are no duplicates, and the maximum length is updated if the current substring is longer than the previously recorded maximum length.
# If duplicates are found, the left pointer is moved to the right to shrink the window until the duplicates are removed.
# The process continues until the right pointer reaches the end of the string. 
# The time complexity is O(n) because each character in the string is processed at most twice (once by each pointer).
# The space complexity is O(n) because the set used to check for duplicates can potentially store all unique characters in the string.