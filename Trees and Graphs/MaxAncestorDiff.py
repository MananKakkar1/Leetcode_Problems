def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # record the required maximum difference
        self.result = 0

        def helper(node, cur_max, cur_min):
            if not node:
                return
            # update `result`
            self.result = max(self.result, abs(cur_max-node.val),
                              abs(cur_min-node.val))
            # update the max and min
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            helper(node.left, cur_max, cur_min)
            helper(node.right, cur_max, cur_min)

        helper(root, root.val, root.val)
        return self.result


# Time Complexity: O(N)
# Space Complexity: O(H) where H is the height of the tree

# We first check if the root is None. If it is, we return 0 as there are no nodes in the tree.
# We initialize a variable `result` to keep track of the maximum difference found.
# We define a helper function that takes a node and the current maximum and minimum values along the path from the root to that node.
# In the helper function, we first check if the node is None. If it is, we return as there is nothing to process.
# We then update the `result` by calculating the maximum of the current `result`, the absolute difference between the current maximum and the node's value, 
# and the absolute difference between the current minimum and the node's value.
# We update the current maximum and minimum values by comparing them with the node's value.
# We recursively call the helper function for the left and right children of the node, passing the updated maximum and minimum values.
# Finally, we call the helper function with the root node and its value as both the current maximum and minimum.
# After the helper function completes, we return the `result` which contains the maximum difference found.
# The time complexity is O(N) because we visit each node exactly once. The space complexity is O(H) where H is the height of the tree, which accounts for the space used by the recursion stack.
