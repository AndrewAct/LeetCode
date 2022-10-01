# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False 
#         if not root.left and not root.right and root.val == targetSum:
#             return True 
#         targetSum -= root.val 
#         return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

# Edited 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root, curr):
            if not root:
                return False
            curr += root.val 
            if not root.left and not root.right:
                return curr == targetSum
            return helper(root.left, curr) or helper(root.right, curr)
        return helper(root, 0)