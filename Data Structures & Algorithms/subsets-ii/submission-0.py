class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        nums.sort()

        def dfs(i, cur):
            if i >= len(nums):
                res.append(curr.copy())
                return

            # include nums[i]
            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()

            # do not include nums[i]
            while (i + 1) < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            dfs(i + 1, curr)

        dfs(0, curr)
        return res
        