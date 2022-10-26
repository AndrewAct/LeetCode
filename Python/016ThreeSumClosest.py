class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return None 
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        n = len(nums)
        curr = sum(nums[:3])
        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                s = sum((nums[i], nums[left], nums[right]))
                if abs(s - target) < abs(curr - target):
                    curr = s 
                if s < target:
                    left += 1 
                elif s > target:
                    right -= 1 
                else:
                    return curr 
        return curr 