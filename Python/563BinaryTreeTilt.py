# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root: return 0
            left_value, right_value = helper(root.left), helper(root.right)
            self.ans += abs(left_value - right_value)
            return root.val + left_value + right_value 
        self.ans = 0 
        helper(root)
        return self.ans