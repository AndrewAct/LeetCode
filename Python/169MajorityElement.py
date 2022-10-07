class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = {}
        for i in nums:
            if i not in my_dict:
                my_dict[i] = 1 
            else:
                my_dict[i] += 1
        max_key = max(my_dict, key=my_dict.get)
        return max_key