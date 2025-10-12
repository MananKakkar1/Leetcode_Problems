class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        visited = set()
        def dfs(x, y):
            if x in visited:
                return False
            visited.add(x)
            for neighbor in adj[x]:
                if neighbor == y:
                    continue
                if not dfs(neighbor, x):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n


