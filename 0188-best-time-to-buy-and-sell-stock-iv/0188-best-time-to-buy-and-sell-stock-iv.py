class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        buy_prices = [float('inf')]*k
        max_profit = [0]*k
        
        for i in range(len(prices)):
            for j in range(k):
                buy_prices[j] = min(buy_prices[j], prices[i] if j == 0 else prices[i]-max_profit[j-1])
                max_profit[j] = max(max_profit[j], prices[i]-buy_prices[j])

        return max_profit[k-1]