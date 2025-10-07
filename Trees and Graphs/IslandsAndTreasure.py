def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr, nc))



# Time Complexity: O(m * n), where m and n are the number of rows and columns in the grid.
# Space Complexity: O(m * n) in the worst case, when all rooms are empty and added to the queue.
#
# This function updates each empty room in the grid with the distance to its nearest gate.
# Each cell can contain a gate (0), a wall (-1), or an empty room (INF, represented by 2147483647).
# The approach uses a multi-source BFS starting from all gates at once.
# First, all gate positions are added to the queue as starting points.
# Then, for each cell removed from the queue, we check its four neighboring cells (up, down, left, right).
# If a neighboring cell is an empty room (INF), we update its value to be the current cell’s distance + 1,
# and add that neighbor to the queue to continue the BFS from there.
# This ensures that each room is updated with the shortest distance to the nearest gate.
# Since every cell is processed at most once, the algorithm runs efficiently in O(m * n).
