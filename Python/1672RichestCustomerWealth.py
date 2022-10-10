class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_res = 0
        for item in accounts:
            max_res = max(max_res, sum(item))
        return max_res 