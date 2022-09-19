# Stack solution
class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        count = 0
        for i in s:
            if i == "(":
                stack.append(i)
            elif i == ")":
                stack.pop()
            else:
                continue 
            count = max(count, len(stack))
        return count 

# Math solution
class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0 
        res = 0
        for i in s:
            if i == "(":
                count += 1 
            elif i == ")":
                count -= 1 
            else:
                continue 
            res = max(count, res)
        return res 