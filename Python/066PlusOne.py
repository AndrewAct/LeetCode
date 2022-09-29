# Method 1: recursion 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        elif len(digits) == 1 and digits[-1] == 9:
            return [1, 0]
        else:
            digits[-1] = 0 
            digits[:-1] = self.plusOne(digits[:-1])
            return digits