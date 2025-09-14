def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if len(stack) > 0 and stack[-1] != char and stack[-1].lower() == char.lower():
                print(char, stack[-1])
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)


# Time Complexity: O(n)
# Space Complexity: O(n)

# Explanation:
# We use a stack to process each character in the string.
# For each character, we check if it can cancel out the top of the stack (i.e., same letter but different cases).
# If it can, we pop the top of the stack; otherwise, we push the current character onto the stack.
# Finally, we join the characters in the stack to form the resulting "good" string.