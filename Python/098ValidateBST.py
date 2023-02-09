# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, -inf, inf)

    def helper(self, root, low, high):
        if not root:
            return True
        if not low < root.val < high:
            return False
        return self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high)