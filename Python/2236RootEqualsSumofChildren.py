# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return 
        if root.val == (root.left.val) + (root.right.val):
            return True 
        return False 

# What if this tree 's depth is more than 1 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def checkTree(self, root: Optional[TreeNode]) -> bool:
#         if not root: return False 
#         if root.left and root.right and root.val != (root.left.val) + (root.right.val):
#             return False
#         self.checkTree(root.left)
#         self.checkTree(root.right)
#         return True 