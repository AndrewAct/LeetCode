# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def sumValue(root, res):
            if root == None: return 0
            res = res * 2 + root.val 
            if root.left == None and root.right == None: return res 
            return sumValue(root.left, res) + sumValue(root.right, res)
        return sumValue(root, 0)