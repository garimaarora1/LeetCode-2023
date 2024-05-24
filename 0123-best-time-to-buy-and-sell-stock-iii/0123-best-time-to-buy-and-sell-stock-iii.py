class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price_1 = buy_price_2 = float('inf')
        max_profit_1 = max_profit_2 = 0
        for price in prices:
            buy_price_1 = min(buy_price_1, price)        
            max_profit_1 = max(max_profit_1, price - buy_price_1)
            buy_price_2 = min(buy_price_2, price-max_profit_1)
            max_profit_2 = max(max_profit_2, price - buy_price_2)
        return max_profit_2
            
        