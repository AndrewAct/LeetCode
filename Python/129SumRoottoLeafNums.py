# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.helper(0,root)
        
    def helper(self, res, root):
        if not root:
            return 0
        res = res * 10 + root.val
        if not root.left and not root.right:
            return res 
        return self.helper(res, root.left) + self.helper(res, root.right)
        