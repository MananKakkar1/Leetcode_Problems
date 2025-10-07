def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0
        def bfs(row, col):
            q = deque()
            grid[row][col] = "0"
            q.append((row, col))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    next_row, next_col = dr + row, dc + col
                    if (next_row < 0 or next_col < 0 or next_row >= rows or
                        next_col >= cols or grid[next_row][next_col] == "0"):
                        continue
                    q.append((next_row, next_col))
                    grid[next_row][next_col] = "0"
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    bfs(row, col)
                    islands += 1
        return islands



# Time Complexity: O(m * n), where m and n are the number of rows and columns in the grid.
# Space Complexity: O(m * n) in the worst case due to the queue used in BFS when the entire grid is land.
#
# This function counts the number of islands in a 2D grid where '1' represents land and '0' represents water.
# It performs a breadth-first search (BFS) to explore all connected land cells that form one island.
# The idea is to scan each cell in the grid; when we find a cell with '1', it marks the start of a new island.
# We then call BFS from that cell, marking all connected land cells as '0' to indicate they’ve been visited.
# The BFS explores in four directions (up, down, left, right) and ensures we stay within grid boundaries.
# Each time BFS finishes, it means one entire island has been visited, so we increment the island count.
# The algorithm continues until every cell in the grid has been processed, and the final count represents
# the total number of distinct islands.