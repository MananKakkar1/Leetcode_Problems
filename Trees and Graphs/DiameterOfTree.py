def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def longest_path(node):
            if not node:
                return -1
            nonlocal diameter
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            diameter = max(diameter, left_path + right_path + 2)

            return max(left_path, right_path) + 1

        longest_path(root)
        return diameter


# Time Complexity: O(N)
# Space Complexity: O(H) where H is the height of the tree

# We define a variable `diameter` to keep track of the maximum diameter found.
# We define a helper function `longest_path` that takes a node as input and returns the length of the longest path from that node to a leaf node.
# In the helper function, we first check if the node is None. If it is, we return -1 as the length of the path.
# We use the `nonlocal` keyword to indicate that we want to modify the `diameter` variable defined in the outer function.
# We recursively call the `longest_path` function for the left and right children of the node to get the lengths of the longest paths from those children to their respective leaf nodes.
# We update the `diameter` by calculating the maximum of the current `diameter` and the sum of the lengths of the longest paths from the left and right children plus 
# 2 (to account for the edges connecting the node to its children).
# We return the length of the longest path from the current node to a leaf node by taking the maximum of the lengths of the longest paths from the left and right children 
# and adding 1 (to account for the edge connecting the node to its child).
# Finally, we call the `longest_path` function with the root node to start the process and return the `diameter` found.