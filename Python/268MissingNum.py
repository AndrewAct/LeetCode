class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        nums = sorted(nums)
        while left < right:
            mid = (right+left)//2
            if (nums[mid]>mid):
                right = mid
            else:
                left = mid+1
        return left