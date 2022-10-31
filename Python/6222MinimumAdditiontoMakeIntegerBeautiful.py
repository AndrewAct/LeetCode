# From Weekly Contest 317 
# You are given two positive integers n and target.

# An integer is considered beautiful if the sum of its digits is less than or equal to target.

# Return the minimum non-negative integer x such that n + x is beautiful. The input will be generated such that it is always possible to make n beautiful.

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        curr = n 
        string = str(n)
        tmp = 0 
        for i in string:
            tmp += int(i)
        if tmp <= target:
            return n-curr
        count = 0 
        while tmp > target:
            if count == 0:
                n = (n // 10 + 1) * 10 
                string1 = str(n)
                tmp1 = 0 
                for i in string1:
                    tmp1 += int(i)
                if tmp1 <= target:
                    return n - curr 
                count += 1 
            else:
                for i in range(count + 1):
                    n //= 10
                n += 1
                new = "0"*(count + 1)
                n = (int(str(n) + new))
                string1 = str(n)
                tmp1 = 0 
                for i in string1:
                    tmp1 += int(i)
                if tmp1 <= target:
                    return n - curr 
                count += 1
            tmp = tmp1
        