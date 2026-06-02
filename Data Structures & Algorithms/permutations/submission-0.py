class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # at each point, you can choose any of the other options
        res = []
        pick = [False for _ in nums]
        curr = []

        def dfs(i, pick, curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if not pick[i]:
                    curr.append(nums[i])
                    pick[i] = True
                    dfs(i, pick, curr)

                    pick[i] = False
                    curr.pop()

        dfs(0, pick, curr)
        return res
            
        