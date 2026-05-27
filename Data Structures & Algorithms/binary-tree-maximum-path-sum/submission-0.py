# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # either a path including root and no split or no root and split
        res = [root.val]
        def dfs(root):
            if not root:
                return 0

            # allows us to ignore negative values
            # what if everything is negative?
            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)

            # computing path with split
            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]