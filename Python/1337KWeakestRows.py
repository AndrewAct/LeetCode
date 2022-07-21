class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        tmp=[]
        for i, n in enumerate(mat):
            res=(sum(n),i) # Get the sum of each row
            # print(res)
            tmp.append(res)
            
        tmp.sort() # Get the tmp in order
        # print(tmp)
        return [i[1] for i in tmp[:k]]