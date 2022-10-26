class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        curr = 0
        dic = {0:-1}
        for i, j in enumerate(nums):
            if k != 0:
                curr = (curr + j) % k 
            else:
                curr += n
            if curr not in dic:
                dic[curr] = i
            else:
                if i - dic[curr] > 1:
                    return True 
        return False 