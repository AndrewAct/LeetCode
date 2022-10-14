# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        my_dict = {}
        def helper(node, target):
            if not node:
                return False
            if node.left and node.right:
                if node.left.val + node.right.val == target:
                    return True 
            if node.val in my_dict:
                return True 
            my_dict[target - node.val] = True 
            return helper(node.left, target) or helper(node.right, target)
        return helper(root, k)