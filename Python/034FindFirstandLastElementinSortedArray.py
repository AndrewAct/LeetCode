class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        if target not in nums:
            return [-1, -1]
        res.append(nums.index(target))
        new_nums = nums[::-1]
        n = len(nums)
        res.append(n - new_nums.index(target)- 1)
        return res