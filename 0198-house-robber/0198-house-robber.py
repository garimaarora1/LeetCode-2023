class Solution:
    def rob(self, h: list[int]) -> int:
        n = len(h)
        dp = [0] * n
        dp[0] = h[0]
        if n==1:
            return h[0]
        
        dp[1] = max(h[0], h[1])
        if n==2:
            return dp[1]
        for i in range(2, n):
            dp[i] = max(dp[i-2] + h[i], dp[i-1])
        return(dp[-1])

        