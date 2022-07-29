class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        a = s.split()
        
        for i in range(len(a)):
            print(a[i][::-1])
            result.append(a[i][::-1])
        return " ".join(result)

class Solution:
    def reverseWords(self, s: str) -> str:
        myList = s.split()
        
        for i in range(len(myList)):
            left, right = 0, len(myList[i])-1 
            
            tmp = list(myList[i])
            while left < right:
                tmp[left], tmp[right] = tmp[right], tmp[left]
                left += 1 
                right -= 1 
            myList[i] = "".join(tmp)
        return " ".join(myList)