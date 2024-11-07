class Solution:
    def lcs(self, text1: str, text2: str) -> int:
        def lcs(i,j):
            if i==m or j==n:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if text1[i]==text2[j]:
                dp[i][j]= 1+lcs(i+1,j+1)
            else:
                dp[i][j]=max(lcs(i+1,j),lcs(i,j+1))
            return dp[i][j]
        m=len(text1)
        n=len(text2)
        dp=[[-1]*(n+1) for i in range(m+1)]
        return lcs(0,0)             

    def longestPalindromeSubseq(self, s: str) -> int :
        return self.lcs(s,s[::-1])