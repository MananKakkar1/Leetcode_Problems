def simplifyPath(self, path: str) -> str:
        pathList = path.split("/")
        stack = []
        for file in pathList:
            if file == '' or file == ".":
                continue
            elif file == "..":
                if stack:
                    stack.pop()
                    if stack and stack[-1] == "/":
                        stack.pop()
                else:
                    stack = []
            else:
                stack.append("/")
                stack.append(file)
        return "".join(stack) if stack != [] else "/"


# Time Complexity: O(n)
# Space Complexity: O(n)

# Explanation:
# We split the input path by "/" to get individual components.
# We use a stack to process each component:
# - Ignore empty components and "." (current directory).
# - For ".." (parent directory), we pop from the stack if it's not empty.
# - For valid directory names, we push them onto the stack with a preceding "/".
# Finally, we join the stack to form the simplified path, ensuring it starts with a "/" or returns "/" if the stack is empty.
