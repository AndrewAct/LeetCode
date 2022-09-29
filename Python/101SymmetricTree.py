# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 
        return self.helper(root.left, root.right)
    
    def helper(self, left, right):
        if left and right:
            return left.val == right.val and self.helper(left.left, right.right) and self.helper(left.right, right.left)
        return left == right