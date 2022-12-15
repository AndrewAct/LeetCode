class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        tmp = [False] * (n+1)
        tmp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if tmp[j] and s[j:i] in wordDict:
                    tmp[i] = True
                    break
        return tmp[-1]