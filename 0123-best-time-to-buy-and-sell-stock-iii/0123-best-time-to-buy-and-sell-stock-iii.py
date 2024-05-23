class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price_1 = buy_price_2 = float('inf')
        sell_price_1, sell_price_2 = 0, 0
        
        for price in prices:
            if price < buy_price_1:
                buy_price_1 = price
            else:
                sell_price_1 = max(sell_price_1, price - buy_price_1)
            
            if price - sell_price_1 < buy_price_2:
                buy_price_2 = price - sell_price_1
            else:
                sell_price_2 = max(sell_price_2, price - buy_price_2)
        return sell_price_2
        
            
            
            