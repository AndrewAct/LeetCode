class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dict = {}
        for i, val in enumerate(nums):
            if val in my_dict and (i - my_dict[val]) <= k:
                return True 
            my_dict[val] = i
        return False 