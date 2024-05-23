class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        if n==0 or k==0:
            return 0
        # do same best time buy 3
        buy=[float('inf')]*k
        sell=[0]*k
        for i in range(n):
            for j in range(k):
                buy[j]=min(buy[j],prices[i] if j==0 else prices[i]-sell[j-1] )
                sell[j]=max(sell[j],prices[i]-buy[j])
        return sell[-1]