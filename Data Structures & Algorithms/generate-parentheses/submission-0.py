class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        combo = []
        open = 0
        closed = 0

        def dfs(combo, open, closed):
            if open == n and closed == n:
                res.append("".join(combo.copy()))
                # open, closed = 0, 0
                return

            # condition 1: add a "("
            if open < n:
                combo.append("(")
                dfs(combo, open + 1, closed)
                combo.pop()

            # condition 2: add a ")"
            if open > closed:
                combo.append(")")
                dfs(combo, open, closed + 1)
                combo.pop()

        dfs(combo, open, closed)
        return res

        