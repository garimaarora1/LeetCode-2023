class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price_1 = buy_price_2 = float('inf')
        max_price_1 = max_price_2 = 0
        
        for price in prices:
            buy_price_1 = min(buy_price_1, price)
            max_price_1 = max(max_price_1, price-buy_price_1)
            buy_price_2 = min(buy_price_2, price-max_price_1)
            max_price_2 = max(max_price_2, price-buy_price_2)
            print(buy_price_1, max_price_1, buy_price_2, max_price_2)
        return max_price_2