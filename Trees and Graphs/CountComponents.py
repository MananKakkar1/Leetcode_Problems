def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(node):
            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    dfs(neighbour)
        count = 0
        seen = set()
        for i in range(n):
            if i not in seen:
                # add all nodes of a connected component to the set
                count += 1
                seen.add(i)
                dfs(i)
        return count



# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
# Space Complexity: O(V + E) for storing the graph and the seen set


# We create an adjacency list representation of the graph using a defaultdict of lists. For each edge (u, v) in the edges list, we add v to the list of u and u to the list of v, since the graph is undirected.
# We define a helper function `dfs` that takes a node as input and performs a depth-first search (DFS) to explore all nodes in the connected component containing that node.
# In the `dfs` function, we iterate through the neighbors of the current node in the graph. For each neighbor, if it has not been seen before, we add it to the `seen` set and recursively call the `dfs` function on that neighbor.
# We initialize a variable `count` to keep track of the number of connected components found and a set `seen` to keep track of the nodes we have already visited.
# We then iterate through all nodes from 0 to n-1. For each node, if it has not been seen before, we increment the `count` by 1 (indicating a new connected component) and add the node to the `seen` set. We then call the `dfs` function on that node to explore all nodes in its connected component.
# Finally, we return the `count` which contains the number of connected components in the graph.
# The time complexity is O(V + E) because we may need to visit all vertices and edges in the worst case. The space complexity is also O(V + E) for storing the graph and the seen set.


