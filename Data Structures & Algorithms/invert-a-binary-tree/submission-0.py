# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # use a recursive solution : flip the two children 
        curr = root
        if not curr:
            return None
            
        temp = curr.left
        curr.left = curr.right
        curr.right = temp

        self.invertTree(curr.left)
        self.invertTree(curr.right)
        
        return root