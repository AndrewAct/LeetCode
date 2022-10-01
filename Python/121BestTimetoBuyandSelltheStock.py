# Initial version 
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         left = 0
#         right = 1 
#         n = len(prices)
#         max_profit = 0
#         while right < n:
#             profit = prices[right] - prices[left]
#             if prices[right] > prices[left]:
#                 max_profit = max(max_profit, profit)
                
#             else:
#                 left = right 
#             right += 1 
#         return max_profit 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit 