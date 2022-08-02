class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res =[]
        
        def track(self, start, comb):
            if (len(comb) == k):
                res.append(comb.copy())
                return 
            
            for i in range(start, n+1):
                comb.append(i)
                track(self,i+1,comb)
                comb.pop()
        track(self,1,[])
        return res