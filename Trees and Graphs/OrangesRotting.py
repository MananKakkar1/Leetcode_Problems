def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        q = deque()
        time = 0
        fresh = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            time += 1
        return time if fresh == 0 else -1



# Time Complexity: O(m * n), where m and n are the number of rows and columns in the grid.
# Space Complexity: O(m * n) in the worst case, when all oranges are rotten and added to the queue.
#
# This function determines the minimum number of minutes required for all fresh oranges in the grid to become rotten.
# Each cell in the grid can contain one of three values:
#   0 → an empty cell
#   1 → a fresh orange
#   2 → a rotten orange
# A rotten orange can rot adjacent fresh oranges (up, down, left, right) in one minute.
#
# The algorithm uses a breadth-first search (BFS) approach starting from all initially rotten oranges.
# It first counts all fresh oranges and adds the positions of all rotten ones to a queue.
# Then, it performs a multi-source BFS where each layer of the queue represents one minute.
# For every orange in the current layer, it rots any adjacent fresh oranges and adds them to the queue for the next layer.
# After processing one layer, the time counter increases by one minute.
# The process continues until there are no fresh oranges left or no more rotting can occur.
#
# If all fresh oranges have become rotten, the total time taken is returned.
# If some fresh oranges remain unreachable (for example, separated by empty cells), the function returns -1.
