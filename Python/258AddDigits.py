class Solution:
    def addDigits(self, num: int) -> int:
        
        while len(str(num)) != 1:
            n = len(str(num))
            tmp = str(num)
            curr = 0
            for i in range(n):
                curr += int(tmp[i])
            num = curr
        return num