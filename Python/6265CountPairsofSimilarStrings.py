class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res = 0 
        n = len(words)
        for i in range(n):
            set1 = sorted(set(words[i]))
            # print(set1)
            for j in range(i+1,n):
                set2 = sorted(set(words[j]))
                # print(set2)
                if set1 == set2:
                    res += 1 
        return res 