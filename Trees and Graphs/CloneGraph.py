def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node) if node else None



# Time Complexity: O(V + E), where V is the number of nodes (vertices) and E is the number of edges in the graph.
# Space Complexity: O(V), for the recursion stack and the hash map that stores the mapping between original and cloned nodes.
#
# This function creates a deep copy (clone) of an undirected graph. Each node in the graph contains a value and a list
# of its neighboring nodes. To avoid duplicating nodes or entering infinite loops in cyclic graphs, the algorithm uses
# a hash map (`oldToNew`) to keep track of already cloned nodes.
# The approach is recursive (DFS). For each node:
# If it has already been copied, return the stored clone from the map.
# Otherwise, create a new node copy, store it in the map, and recursively clone all its neighbors.
# This ensures that every node and its connections are duplicated exactly once, maintaining the same structure
# as the original graph. If the input node is None, the function simply returns None.
