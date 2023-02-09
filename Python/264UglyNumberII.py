class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2, i3, i5 = 0, 0, 0
        next2, next3, next5 = 2, 3, 5
        ugly = [1]
        for i in range(n):
            nextAdd = min(next2, next3, next5)
            ugly.append(nextAdd)
            if nextAdd == next2:
                i2 += 1 
                next2 = ugly[i2]*2 
            if nextAdd == next3:
                i3 += 1 
                next3 = ugly[i3]*3 
            if nextAdd == next5:
                i5 += 1 
                next5 = ugly[i5]*5
        return ugly[n-1]