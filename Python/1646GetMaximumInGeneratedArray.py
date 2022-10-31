# class Solution:
#     def getMaximumGenerated(self, n: int) -> int:
#         if n < 0:
#             return None 
#         if n <= 1:
#             return n 
#         nums = [0] * (n + 1)
#         i = 0
#         while i <= n:
#             if i <= 1:
#                 nums[i] = i
#             elif i > 1 and i % 2 == 0:
#                 nums[i] = nums[i//2]
#             else:
#                 nums[i] = nums[i//2] + nums[i//2+1]
#             i += 1 
#         # print(nums)
#         return max(nums)

# Modified:
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0] * (n + 2)
        nums[1] = 1 
        if n <= 1: return n
        for i in range(2, n+1):
            nums[i] = nums[i // 2] + nums[i//2 + 1] * (i%2 )
        return max(nums)