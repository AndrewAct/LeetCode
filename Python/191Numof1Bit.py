class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0 
        for i in range(32):
            num += (n & 1)
            n = n >> 1
        return num 