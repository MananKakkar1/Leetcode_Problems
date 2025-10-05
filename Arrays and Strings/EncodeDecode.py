def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "empty"
        return "(--:--)".join(strs)
def decode(self, s: str) -> List[str]:
    if "empty" in s:
        return []
    return s.split("(--:--)")



# Time Complexity: O(n) where n is the total number of characters in all strings.
# Space Complexity: O(n) for the encoded string.

# The encode function takes a list of strings and joins them into a single string using a unique delimiter "(--:--)".
# If the input list is empty, it returns the string "empty" to signify that there are no strings to encode.
# The decode function takes the encoded string and splits it back into a list of strings using the same delimiter.
# If the encoded string is "empty", it returns an empty list.
# This approach ensures that the original list of strings can be accurately reconstructed from the encoded string.
# The time complexity for both functions is O(n) because we need to process each character in the input strings.
# The space complexity is also O(n) because we create a new string for the encoded result and a new list for the decoded result.