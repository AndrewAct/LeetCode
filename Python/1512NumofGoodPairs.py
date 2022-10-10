# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         n = len(nums)
#         res = 0
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 if nums[j] == nums[i]:
#                     res += 1 
#                 else:
#                     j += 1 
#         return res 

# Modified:
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        my_dict = {}
        res = 0
        for num in nums:
            if num in my_dict:
                if my_dict[num] == 1:
                    res += 1 
                else:
                    res += my_dict[num]
                my_dict[num] += 1
            else:
                my_dict[num] = 1 
        return res 