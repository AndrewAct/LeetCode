class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        neg, pos, zero = [], [], []
        
        for i in nums:
            if i < 0:
                neg.append(i)
            elif i > 0:
                pos.append(i)
            else:
                zero.append(i)
        set_neg = set(neg)
        set_pos = set(pos)
        if len(zero) > 2:
            res.add((0,0,0))
            
        if zero:
            for item in set_pos:
                if (-1*item in set_neg):
                    res.add((-1*item, 0, item))
        
        for i in range(len(neg)):
            for j in range(i+1, len(neg)):
                target = -1*(neg[i]+ neg[j])
                if target in set_pos:
                    res.add(tuple(sorted([neg[i], neg[j], target])))
        
        for i in range(len(pos)):
            for j in range(i+1,len(pos)):
                target = -1*(pos[i]+ pos[j])
                if target in set_neg:
                    res.add(tuple(sorted([pos[i], pos[j], target])))
                    
                    
        return res