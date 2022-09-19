class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return None 
        if numRows == 1:
            return [[1]]
        res = [0]* numRows 
        for i in range(numRows):
            res[i] = [0]* (i+1)
            for j in range(i+1):
                if (i==j) or (j==0):
                    res[i][j] = 1 
                else:
                    res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res 