class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count_pos, count_neg = 0, 0 
        for i in operations:
            if (i == "++X") or (i == "X++"):
                count_pos += 1
            else:
                count_neg += 1 
        return count_pos - count_neg

# Dictionary method:
# class Solution:
#     def finalValueAfterOperations(self, operations: List[str]) -> int:
#         my_dict = {"X++":1, "++X":1, "X--":-1,"--X":-1}
#         return sum(my_dict[op] for op in operations)