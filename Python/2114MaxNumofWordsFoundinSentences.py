# class Solution:
#     def mostWordsFound(self, sentences: List[str]) -> int:
#         max_len = 0
#         for element in sentences:
#             res = element.split()
#             max_len = max(max_len, len(res))
#         return max_len 

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(element.split()) for element in sentences)