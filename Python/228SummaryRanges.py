class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res, i, start = [], 0 , 0
        while i < len(nums)-1:
            if nums[i]+1 != nums[i+1]:
                res.append(self.printer(nums[start], nums[i]))
                start = i+1
            i += 1
        res.append(self.printer(nums[start], nums[i]))
        return res
    
    
    def printer(self, l, r):
        if l == r:
            return str(l)
        else:
            return str(l) + "->" + str(r)