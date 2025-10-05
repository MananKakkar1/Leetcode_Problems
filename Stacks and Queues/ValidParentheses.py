def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if stack != [] and char == ')' and '(' == stack[-1]:
                stack.pop()
            elif stack != [] and char == '}' and '{' == stack[-1]:
                stack.pop()
            elif stack != [] and char == ']' and '[' == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return stack == []



# Time Complexity: O(n) where n is the length of the string s.
# Space Complexity: O(n) in the worst case when all characters are opening brackets.

# The function uses a stack to keep track of opening brackets.
# It iterates through each character in the string s.
# When it encounters a closing bracket, it checks if the top of the stack contains the corresponding opening bracket.
# If it does, it pops the top of the stack. If not, it pushes the closing bracket onto the stack.
# If the character is an opening bracket, it is pushed onto the stack.
# After processing all characters, if the stack is empty, it means all brackets were matched correctly, and the function returns True. Otherwise, it returns False.
# The time complexity is O(n) because we process each character in the string once.
# The space complexity is O(n) in the worst case when all characters are opening brackets, as they will all be stored in the stack.
