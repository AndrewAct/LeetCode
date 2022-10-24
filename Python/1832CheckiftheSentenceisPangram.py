class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26


# import string

# class Solution:
#     def checkIfPangram(self, sentence: str) -> bool:
#         if len(sentence) < 26: return False
#         my_ls = list(string.ascii_lowercase)
#         for item in sentence:
#             if item in my_ls:
#                 my_ls.remove(item)
#         return len(my_ls) == 0