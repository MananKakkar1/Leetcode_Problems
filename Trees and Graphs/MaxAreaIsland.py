def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        area = 0
        def bfs(row, col):
            result = 1
            q = deque()
            grid[row][col] = 0
            q.append((row, col))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    next_row, next_col = dr + r, dc + c
                    if next_row < 0 or next_col < 0 or next_row >= rows or next_col >= cols or grid[next_row][next_col] == 0:
                        continue
                    q.append((next_row, next_col))
                    grid[next_row][next_col] = 0
                    result += 1
            return result
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = max(area, bfs(row, col))
        return area



# Time Complexity: O(m * n), where m and n are the number of rows and columns in the grid.
# Space Complexity: O(m * n) in the worst case, due to the BFS queue when the entire grid is land.
#
# This function finds the maximum area of an island in a 2D grid where 1 represents land and 0 represents water.
# An island is a group of connected 1s (horizontally or vertically). The algorithm uses BFS to explore each island
# and calculate its area by counting all the connected land cells.
# It scans the entire grid, and whenever it encounters a land cell (1), it performs BFS starting from that cell.
# During BFS, each visited land cell is marked as 0 to avoid revisiting it, and we count how many land cells are part
# of that island. The result of BFS represents the area of the current island.
# After exploring one island, the algorithm compares its area with the maximum area found so far.
# Once all cells have been processed, the largest recorded area is returned as the final answer.
