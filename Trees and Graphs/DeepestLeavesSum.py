def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        q = deque([(root, 0)])
        leaves = []
        max_depth = 0
        while q:
            node, depth = q.popleft()
            if not node.left and not node.right:
                if depth > max_depth:
                    max_depth = depth
                    leaves = [node.val]
                elif depth == max_depth:
                    leaves.append(node.val)
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
        return sum(leaves)


# Time Complexity: O(N)
# Space Complexity: O(N)

# We use a breadth-first search (BFS) approach to traverse the tree level by level.
# We initialize a queue with the root node and its depth (0).
# We also initialize an empty list `leaves` to store the values of the deepest leaves and a variable `max_depth` to keep track of the maximum depth found.
# We enter a while loop that continues until the queue is empty.
# In each iteration, we pop the first element from the queue, which gives us the current
# node and its depth.
# We check if the current node is a leaf node (i.e., it has no left or right children). If it is, we compare its depth with `max_depth`.
# If the depth is greater than `max_depth`, we update `max_depth` and reset the `leaves` list to contain only the current node's value.
# If the depth is equal to `max_depth`, we append the current node's value to the `leaves` list.
# If the current node has a left child, we append it to the queue with an incremented depth.
# Similarly, if the current node has a right child, we append it to the queue with an incremented depth.
# This process continues until we have traversed all nodes in the tree.
# Finally, we return the sum of the values in the `leaves` list, which contains the values of the deepest leaves.
# The time complexity is O(N) because we visit each node exactly once. The space complexity is O(N) in the worst case, where the tree is completely unbalanced and the queue contains all nodes at the deepest level.