def maxNumberOfBalloons(self, text: str) -> int:
        seen = {}
        for ch in text:                     
            seen[ch] = seen.get(ch, 0) + 1

        return min(
            seen.get('b', 0),
            seen.get('a', 0),
            seen.get('l', 0) // 2,
            seen.get('o', 0) // 2,
            seen.get('n', 0),
        )


# Time Complexity : O(n) where n is the length of the text
# Space Complexity : O(1) since the size of the hashmap will be at max

# Explanation: We create a hashmap to store the characters in the text.
# We then iterate through the text and add each character to the hashmap.
# We use the get method of the dictionary to return 0 if the character is not found in the hashmap.
# Finally, we return the minimum count of the characters needed to form the word "balloon
# (b, a, l, o, n) with l and o needing to be counted twice.
