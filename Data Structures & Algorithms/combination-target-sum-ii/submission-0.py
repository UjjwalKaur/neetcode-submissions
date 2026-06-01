class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # same base cases as prev problem 
        res = []
        total = 0
        curr = []
        candidates.sort()

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            if i >= len(candidates) or total > target:
                return 

            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])

            curr.pop()

            # when skipping candidates, we also need to skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr, total)

        dfs(0, curr, total)
        return res