class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        capitals = [chr(x) for x in range(ord('A'),ord('Z')+1)]
        res = []
        while columnNumber > 0:
            res.append(capitals[(columnNumber - 1) % 26])
            columnNumber = (columnNumber - 1) // 26
        res.reverse()  
        return ''.join(res)