class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        count = 0
        for item in s:
            if item == "(":
                count += 1 
                if count > 1:
                    res += "("
            if item == ")":
                count -= 1
                if count > 0:
                    res += ")"
        return res 