class Solution:
    def minDeletions(self, s: str) -> int:
        freq = {}
        for i in s:
            freq[i] = 1 + freq.get(i, 0)
        ans = 0
        seen = set()
        for k in freq.values():
            while k in seen:
                k -= 1 
                ans += 1 
            if k: seen.add(k)
        return ans 