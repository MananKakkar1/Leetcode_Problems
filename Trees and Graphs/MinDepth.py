def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [(root, 1)]
        min_depth = float('inf')
        while queue:
            curr, depth = queue.pop(0)
            if not curr.left and not curr.right:
                return min(min_depth, depth)
            if curr.left:
                queue.append((curr.left, depth + 1))
            if curr.right:
                queue.append((curr.right, depth + 1))


# Time Complexity: O(N)
# Space Complexity: O(N)

# Firstly, we check if the root is None. If it is, we return 0 as the minimum depth.
# We solve this using a breadth-first search (BFS) approach.
# We initialize a queue with the root node and its depth (1).
# We also initialize min_depth to infinity to keep track of the minimum depth found.
# We then enter a while loop that continues until the queue is empty.
# In each iteration, we pop the first element from the queue, which gives us the current node and its depth.
# We check if the current node is a leaf node (i.e., it has no left or right children). If it is, we return the minimum of the current min_depth and the depth of this leaf node.
# If the current node has a left child, we append it to the queue with an incremented depth.
# Similarly, if the current node has a right child, we append it to the queue with an incremented depth.
# This process continues until we find the first leaf node, at which point we return its depth as the minimum depth of the tree.
# The time complexity is O(N) because we may need to visit all nodes in the worst case. The space complexity is also O(N) due to the queue storing nodes at each level of the tree.
 