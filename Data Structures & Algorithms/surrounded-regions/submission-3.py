class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                board[r][c] != "O"):
                return
            
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Check O's in left/right borders, and sink the connected 0's
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)

        # check for O's in top/bottom borders, and sink the connected 0's
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)
        
        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"


