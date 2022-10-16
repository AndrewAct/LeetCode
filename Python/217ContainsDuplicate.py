from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_dict = defaultdict(int)
        for item in nums:
            my_dict[item] = 1+ my_dict.get(item, 0)
            if my_dict[item] > 1:
                return True 
        return False 

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return len(nums) != len(set(nums))