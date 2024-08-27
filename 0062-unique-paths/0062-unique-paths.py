class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = m
        col = n
        
        dp = [[0] * col for _ in range(row)]
        
        for i in range(row):
            dp[i][0] = 1
        
        for j in range(col):
            dp[0][j] = 1
        
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[row-1][col-1]
        