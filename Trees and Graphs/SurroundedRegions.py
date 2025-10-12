class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        def dfs(r, c):
            if (r < 0 or r > ROWS - 1 or c < 0 or c > COLS - 1 
               or board[r][c] != "O"):
                return
            board[r][c] = "T"
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"