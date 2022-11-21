class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        curr = 1 
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                continue 
            nums[curr] = nums[i]
            curr += 1
        return curr
        