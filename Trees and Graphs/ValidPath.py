def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if edges == [] and source == destination:
            return True
        elif edges == []:
            return False
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set([source])
        stack = [source]
        while stack:
            curr = stack.pop()
            if curr == destination:
                return True
            for neighbour in graph[curr]:
                if neighbour not in seen:
                    stack.append(neighbour)
                    seen.add(neighbour)
        if destination not in seen:
            return False
        return True



# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
# Space Complexity: O(V + E) for storing the graph and the seen set

# We first check if the edges list is empty. If it is and the source is equal to the destination, we return True as there is a valid path (the source is the destination). If the edges list is empty and the source is not equal to the destination, we return False as there is no valid path.
# We then create an adjacency list representation of the graph using a defaultdict of lists. For each edge (u, v) in the edges list, we add v to the list of u and u to the list of v, since the graph is undirected.
# We initialize a set `seen` to keep track of the nodes we have already visited, starting with the source node. We also initialize a stack with the source node to facilitate depth-first search (DFS).
# We enter a while loop that continues until the stack is empty. In each iteration, we pop the last node from the stack and check if it is equal to the destination. If it is, we return True as we have found a valid path.
# If the current node is not the destination, we iterate through its neighbors in the graph. For each neighbor, if it has not been seen before, we add it to the stack and mark it as seen.
# This process continues until we either find the destination or exhaust all possible paths.
# After the while loop, we check if the destination is in the seen set. If it is not, we return False as there is no valid path from the source to the destination. If it is, we return True.
# The time complexity is O(V + E) because we may need to visit all vertices and edges in the worst case. The space complexity is also O(V + E) for storing the graph and the seen set.