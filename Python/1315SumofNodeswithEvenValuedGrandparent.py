# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.res = 0
       
        def dfs(root):
            if not root:
                return 0
            if root.val % 2 == 0:
                if root.left:
                    if root.left.left:
                        self.res += root.left.left.val 
                    if root.left.right:
                        self.res += root.left.right.val
                
                if root.right:
                    if root.right.right:
                        self.res += root.right.right.val 
                    if root.right.left:
                        self.res += root.right.left.val 
                        
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            
        dfs(root)
        return self.res 