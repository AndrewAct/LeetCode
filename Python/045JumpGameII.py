class Solution:
    def jump(self, nums: List[int]) -> int:
        jump, curEnd, nextEnd = 0, 0, 0
        n = len(nums)
        for i in range(n-1):
            nextEnd = max(nextEnd, nums[i] + i)
            if i == curEnd:
                jump += 1 
                curEnd = nextEnd 
        return jump