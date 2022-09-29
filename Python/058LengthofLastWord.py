class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        my_list = s.split()
        if my_list:
            return len(my_list[-1])
        return 0