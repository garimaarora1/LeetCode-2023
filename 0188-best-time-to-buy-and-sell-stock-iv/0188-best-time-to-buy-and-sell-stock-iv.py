class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy_price = [float('inf')] * (k)
        max_profit = [0] * (k)
        for i in range(len(prices)):
            for j in range(k):
                buy_price[j] = min(buy_price[j], prices[i] if j == 0 else prices[i]-max_profit[j-1])
                max_profit[j] = max(max_profit[j], prices[i]-buy_price[j])
        return max_profit[-1]
        