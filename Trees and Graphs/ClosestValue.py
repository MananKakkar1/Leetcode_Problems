def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        node = root
        
        while node:
            if (abs(node.val - target) < abs(closest - target) or
               (abs(node.val - target) == abs(closest - target) and node.val < closest)):
                closest = node.val
            
            if target < node.val:
                node = node.left
            else:
                node = node.right
        
        return closest


# Time Complexity: O(H) where H is the height of the tree
# Space Complexity: O(1)

# We initialize a variable `closest` to keep track of the closest value found so far, starting with the root's value.
# We also initialize a variable `node` to traverse the tree, starting with the root node.
# We enter a while loop that continues until `node` is None.
# In each iteration, we check if the absolute difference between the current node's value and the target is less than the absolute difference between `closest` and the target.
# If it is, we update `closest` to the current node's value.
# If the absolute differences are equal, we check if the current node's value is less than `closest`, and if so, we update `closest` to the current node's value.
# We then decide whether to traverse to the left or right child of the current node based on the comparison between the target and the current node's value.
# If the target is less than the current node's value, we move to the left child; otherwise, we move to the right child.
# This process continues until we reach a leaf node (i.e., `node` becomes None).
# Finally, we return the `closest` value found.
# The time complexity is O(H) where H is the height of the tree, as we may need to traverse from the root to a leaf node in the worst case.
# The space complexity is O(1) since we are using only a constant amount of extra space.