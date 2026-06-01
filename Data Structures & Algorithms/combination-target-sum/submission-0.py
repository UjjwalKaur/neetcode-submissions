class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        total = 0

        def dfs(i, curr, total):
            if total > target or i >= len(nums):
                return

            if total == target:
                res.append(curr.copy())
                return

            # condition 1 : include nums[i]
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.remove(nums[i])

            # condition 2 : increment i
            dfs(i + 1, curr, total)

        dfs(0, curr, total)
        return res
        