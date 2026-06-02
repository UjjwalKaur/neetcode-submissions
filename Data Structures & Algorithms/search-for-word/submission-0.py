class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(curr, r, c):
            if curr == len(word):
                return True

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[curr] or (r, c) in path):
                return False

            path.add((r, c))
            res =  dfs(curr + 1, r - 1, c) or dfs(curr + 1, r + 1, c) or dfs(curr + 1, r, c - 1) or dfs(curr + 1, r, c + 1)

            path.remove((r, c))
            return res


        for r in range(ROWS):
            for c in range(COLS):
                res = dfs(0, r, c)
                if res:
                    return True

        return False




        