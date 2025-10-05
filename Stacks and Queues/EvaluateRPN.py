def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(token))
        return stack[0]



# Time Complexity: O(n) where n is the number of tokens.
# Space Complexity: O(n) in the worst case when all tokens are numbers.

# The function uses a stack to evaluate the expression in Reverse Polish Notation (RPN).
# It iterates through each token in the input list.
# If the token is an operator (+, -, *, /), it pops the top two numbers from the stack, applies the operator, and pushes the result back onto the stack.
# If the token is a number, it converts it to an integer and pushes it onto the stack.
# After processing all tokens, the final result of the RPN expression is the only number left in the stack, which is returned.
# The time complexity is O(n) because each token is processed once.
# The space complexity is O(n) in the worst case when all tokens are numbers, as they will all be stored in the stack.
