def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                n = board[r][c]
                if (n in rows[r]) or (n in cols[c]) or (n in boxes[r//3][c//3]):
                    return False
                rows[r].add(n)
                cols[c].add(n)
                boxes[r//3][c//3].add(n)
        return True


# Time Complexity: O(1)
# Space Complexity: O(1)


# The function initializes three lists of sets to keep track of the numbers seen in each row, column, and 3x3 sub-box.
# It then iterates through each cell in the 9x9 board. If the cell contains a number (not a '.'), it checks if that number has already been seen in the corresponding row, column, or sub-box.
# If the number has been seen before in any of these, the function returns False, indicating the board is not valid.
# If the number has not been seen, it adds the number to the respective row, column, and sub-box sets.
# If the loop completes without finding any duplicates, the function returns True, indicating the board is valid.
# The time complexity is O(1) because the board size is fixed (9x9), so the number of operations does not scale with input size.
# The space complexity is also O(1) for the same reason, as the maximum space used is constant regardless of input size.
# The use of sets allows for O(1) average time complexity for both insertions and lookups, making the checks efficient.
# The function effectively checks all Sudoku rules in a single pass through the board.

