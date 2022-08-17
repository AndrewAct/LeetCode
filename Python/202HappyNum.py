class Solution:
    def isHappy(self, n: int) -> bool:
        mySet = set()
        while n not in mySet:
            mySet.add(n)
            n = sum([int(x) **2 for x in str(n)])
        return n == 1
