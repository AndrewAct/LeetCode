class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        left, right = 0, 0
        # length = len(s)
        strList = list(s)
        res = 0
        while (right < len(s)):
            if not (strList[right] in mySet):
                mySet.add(strList[right])
                right += 1
                res = max(res, len(mySet))
            else:
                mySet.remove(strList[left])
                left += 1 
        return max(len(mySet),res)

# Runtime: 150 ms, faster than 25.43% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.3 MB, less than 5.03% of Python3 online submissions for Longest Substring Without Repeating Characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        left = 0
        res = 0
        # length = len(s)
        
        for right in range(len(s)):
            while (s[right] in mySet):
                mySet.remove(s[left])
                left += 1 
            mySet.add(s[right])
            res = max(res, right-left+1)
        return res 

# Runtime: 120 ms, faster than 39.04% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14 MB, less than 93.05% of Python3 online submissions for Longest Substring Without Repeating Characters.