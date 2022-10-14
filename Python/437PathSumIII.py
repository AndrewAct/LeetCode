# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        global res
        res = 0 
        
        def dfs(node, target):
            if not node: return 
            helper(node, target)
            dfs(node.left, target)
            dfs(node.right, target)
        
        def helper(node, target):
            global res
            if not node:
                return 
            if node.val == target:
                res += 1
            helper(node.left, target - node.val)
            helper(node.right, target - node.val)    
            
        dfs(root, targetSum)
        return res 