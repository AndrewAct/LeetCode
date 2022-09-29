class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l1 = self.helper(s, [])
        l2 = self.helper(t, [])
        return l1 == l2
        
    def helper(self, my_input, stack):
        for item in my_input:
            if item is not "#":
                stack.append(item)
            else:
                if not stack:
                     continue 
                stack.pop()
                #print(stack)
        return stack