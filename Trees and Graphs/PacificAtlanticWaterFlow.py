class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pacific, atlantic = set(), set()

        def dfs(row, col, visited, prevHeight):
            if (
                row < 0 or row >= len(heights) or 
                col < 0 or col >= len(heights[0]) or 
                (row, col) in visited or 
                heights[row][col] < prevHeight
            ):
                return
            visited.add((row, col))
            for dr, dc in directions:
                dfs(row + dr, col + dc, visited, heights[row][col])

        for c in range(len(heights[0])):
            dfs(0, c, pacific, heights[0][c])
            dfs(len(heights) - 1, c, atlantic, heights[len(heights) - 1][c])

        for r in range(len(heights)):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, len(heights[0]) - 1, atlantic, heights[r][len(heights[0]) - 1])
        
        result = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if ((r, c) in pacific and (r, c) in atlantic):
                    result.append([r, c])
        return result



