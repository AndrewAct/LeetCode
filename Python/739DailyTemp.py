# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         n = len(temperatures)
#         myList = [0]*n
#         i = n
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 if temperatures[j] > temperatures[i]:
#                     myList[i] = j-i
#                     break 
            
        
#         return myList 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                #print(stack[-1][0])
                stackT, stackI = stack.pop()
                res[stackI] = (i - stackI)
            stack.append([t,i])
        return res 