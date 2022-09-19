class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        res = [0]*(rowIndex+1)
        for i in range(rowIndex+1):
            res[i] = [0]* (rowIndex + 1)
            for j in range(i+1):
                if (i == j) or (j == 0):
                    res[i][j] = 1 
                else:
                    res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res[rowIndex]