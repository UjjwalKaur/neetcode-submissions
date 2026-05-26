# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # calculate balance factor recursively using dfs
        # calculate height of children on the left and right side and subtract

        def dfs(root):
            if not root:
                return [True, 0]

            balanced = True

            left = dfs(root.left)
            right = dfs(root.right)
            height = max(left[1], right[1]) + 1
            
            if (left[0] and right[0] and abs(left[1] - right[1]) <= 1):
                balanced = True
            else:
                balanced = False

            return [balanced, height]

        return dfs(root)[0]
        