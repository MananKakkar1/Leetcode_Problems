def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)
        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                res = max(res, r - l + 1)
        return res



# Time Complexity: O(26 * n) which simplifies to O(n), where n is the length of the string s.
# Space Complexity: O(1) since the size of the character set is fixed (26 letters in the English alphabet).

# The function uses a sliding window approach to find the length of the longest substring that can be obtained by replacing at most k characters to make all characters in the substring the same.
# It iterates through each unique character in the string and uses two pointers (left and right) to represent the current window of characters being considered.
# For each character, it counts how many times that character appears in the current window and calculates the number of characters that need to be replaced to make all characters in the window the same.
# If the number of characters to be replaced exceeds k, it moves the left pointer to the right to shrink the window until the condition is satisfied again.
# The maximum length of the valid window is updated during each iteration.
# The time complexity is O(26 * n) because for each of the 26 possible characters, the algorithm processes the string with a sliding window approach, resulting in a linear scan of the string.
# The space complexity is O(1) because the character set size is constant and does not scale with the input size.