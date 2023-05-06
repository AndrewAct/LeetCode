class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        list1, list2 = list(word1), list(word2)
        len_ = len1 + len2 
        res = [] 
        while list1 and list2:
            res.append(list1.pop(0))
            res.append(list2.pop(0))
        if not list1 and not list2:
            return "".join(res)
        elif not list2:
            res.extend(list1)
        else:
            res.extend(list2)
        # return "".join(str(e) for e in res)
        return "".join(res)