# from collections import defaultdict
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         dict_1, dict_2 = defaultdict(int), defaultdict(int)
#         for i in s:
#             if i not in dict_1:
#                 dict_1[i] = 0
#             dict_1[i] = dict_1.get(i, 0) + 1
#         for j in t:
#             if j not in dict_2:
#                 dict_2[j] = 0
#             dict_2[j] = dict_2.get(j, 1) + 1
#         print(dict_1)
#         print(dict_2)
#         return dict_1 == dict_2


from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)