# [7, 2, 5, 1, 6, 4]
#                 S
#
#
# min_sale = 1
# max_profti = 5


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = -1
        min_sale = float('inf')
        for price in prices:
            min_sale = min(min_sale, price)
            max_profit = max(max_profit, (price - min_sale))
        
        return max_profit
            
            