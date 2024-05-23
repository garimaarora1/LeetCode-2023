class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        max_diff = 0
        for price in prices[1:]:
            if price <= mini:
                mini = price
            else:
                max_diff += (price - mini)
                mini = price
        return max_diff