class Solution:
    def numSquares(self, n: int) -> int:
        dp=[float('inf')-1]*(n+1)
        dp[0]=0
        squares = []
        for i in range(n//2 + 2):
            if i*i <= n:
                squares.append(i*i)
            
        for i in range(n+1):
            for square in squares:
                if i>=square:
                    dp[i]=min(dp[i],dp[i-square]+1)                    
        return dp[n] if dp[n]!=float('inf')-1 else -1
        