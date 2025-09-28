def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        
        return root


# Time Complexity: O(H) where H is the height of the tree
# Space Complexity: O(H) due to the recursion stack

# We first check if the root is None. If it is, we create a new TreeNode with the given value and return it as the new root of the BST.
# If the root is not None, we compare the given value with the value of the current root node.
# If the given value is greater than the root's value, we recursively call the insertIntoBST function on the right subtree of the root.
# If the given value is less than or equal to the root's value, we recursively call the insertIntoBST function on the left subtree of the root.
# After the recursive call, we assign the returned subtree to the appropriate child (left or right  of the root).
# Finally, we return the root of the modified BST.
# The time complexity is O(H) where H is the height of the tree, as we may need to traverse from the root to a leaf node in the worst case.
# The space complexity is also O(H) due to the recursion stack, which can go as deep as the height of the tree.