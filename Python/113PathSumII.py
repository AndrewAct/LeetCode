# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        self.helper(root, [], ans, targetSum)
        return ans
    
    def helper(self, root, path, ans, remaining):
        if not root:
            return []
        path.append(root.val)
        if not root.left and not root.right and remaining == root.val:
            ans.append(list(path))
        self.helper(root.left, path, ans, remaining - root.val)
        self.helper(root.right, path, ans, remaining - root.val)
        path.pop()