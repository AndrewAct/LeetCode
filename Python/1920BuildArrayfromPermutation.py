class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # tmp = [0]* n 
        tmp = [nums[i] for i in range(n)]
        res = [nums[j] for j in tmp]
        return res

# Faster than 94.17% Pythn3 submissions