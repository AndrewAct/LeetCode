# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         left, right = 0, 1 
#         n = len(prices)
#         maxProfit = 0
#         for i in range(n-1):
#             if prices[i+1] > prices[i]:
#                 maxProfit += (prices[i+1] - prices[i])
#         return maxProfit 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0]*n 
        for i in range(1,n):
            dp[i] = dp[i-1] + max(0, prices[i]-prices[i-1])
        return dp[n-1]