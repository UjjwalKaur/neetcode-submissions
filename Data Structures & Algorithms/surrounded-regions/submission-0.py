class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS = len(board)
        COLS = len(board[0])

        # if neighbors of 0 are 0, it is part of the central region
        # if not, it is part of the border

        # if a group of 0s is connected to the border
        # it is not a surrounded 0

        from collections import deque

        q = deque()
        q.append((0,0))

        def dfs(r, c):
            # base case --> think about this as when you want the recursion to stop
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != 'O'):
                return
            else:
                board[r][c] = 'T'
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        for r in range(ROWS):
            if (board[r][0] == 'O'):
                dfs(r, 0)
            if (board[r][COLS - 1] == 'O'):
                dfs(r, COLS - 1)

        for c in range(COLS):
            if(board[0][c] == 'O'):
                dfs(0, c)
            if (board[ROWS - 1][c] == 'O'):
                dfs(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if(board[r][c] == 'O'):
                    board[r][c] = 'X'
                elif (board[r][c] == 'T'):
                    board[r][c] = 'O'

