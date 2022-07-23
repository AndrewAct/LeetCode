class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # nums = sorted(nums)
        return sorted([i**2 for i in nums])