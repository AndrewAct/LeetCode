class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        countS1 = Counter(s1)
        
        for i in range(len(s2) - window + 1):
            if Counter(s2[i:(i+window)]) == countS1:
                return True 
        
        return False