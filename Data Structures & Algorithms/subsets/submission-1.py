class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for an array of length size, number of elements in the subset must be 2^size
        # use backtracking using recursive dfs
        res = []
        subset = []

        def dfs(i):
            # base case
            if (i >= len(nums)):
                # adding a copy instead otherwise it would just point to the current changed value of subset
                res.append(subset.copy())
                return 

            # decision : include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision : do not include nums[i]
            subset.remove(nums[i])
            dfs(i + 1)

        dfs(0)
        return res



        