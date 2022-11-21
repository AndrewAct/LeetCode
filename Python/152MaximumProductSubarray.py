class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_end, max_now, min_now = nums[0], nums[0], nums[0]
        n = len(nums)
        for i in range(1, n):
            tmp = max_now 
            max_now = max(nums[i], max(nums[i]*max_now, nums[i]*min_now))
            min_now = min(nums[i], min(nums[i]*tmp, nums[i]*min_now))
            max_end = max(max_end, max_now)
        return max_end