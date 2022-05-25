class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = []
        i = 0
        for e in pushed:
            s.append(e)
            #print(s)
            while s and s[-1] == popped[i]:
                s.pop()
                #print(s)
                i += 1
        return i == len(popped)