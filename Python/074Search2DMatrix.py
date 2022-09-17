class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m*n - 1 
        while low <= high:
            mid = (low + high) // 2
            curr = matrix[mid//n][mid % n]
            if curr == target:
                return True 
            if curr < target:
                low += 1 
            else:
                high -= 1
        return False