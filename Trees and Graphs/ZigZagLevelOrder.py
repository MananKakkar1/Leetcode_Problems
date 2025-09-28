def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import deque

        q = deque([root])
        left_to_right = True
        result = []

        while q:
            level = deque()
            for _ in range(len(q)):
                node = q.popleft()
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(list(level))
            left_to_right = not left_to_right

        return result


# Time Complexity: O(N)
# Space Complexity: O(N)


# We first check if the root is None. If it is, we return an empty list as there are no nodes in the tree.
# We use a deque (double-ended queue) to facilitate efficient popping from the front and appending to both ends.
# We initialize a boolean variable `left_to_right` to keep track of the current direction of traversal.
# We also initialize an empty list `result` to store the final zigzag level order traversal.
# We enter a while loop that continues until the queue is empty.
# In each iteration, we create a new deque `level` to store the values of the current level.
# We then iterate over the nodes in the current level (the number of nodes is determined by the length of the queue).
# For each node, we pop it from the front of the queue and check the current direction.
# If `left_to_right` is True, we append the node's value to the right end of the `level` deque.
# If `left_to_right` is False, we append the node's value to the left end of the `level` deque.
# We then check if the node has left and right children. If it does, we append them to the queue for processing in the next level.
# After processing all nodes in the current level, we convert the `level` deque to a list and append it to the `result` list.
# We toggle the `left_to_right` variable to change the direction for the next level.
# Finally, we return the `result` list which contains the zigzag level order traversal of the tree.
# The time complexity is O(N) because we visit each node exactly once. The space complexity is O(N) in the worst case, where the tree is completely unbalanced and the queue contains all nodes at the deepest level.
