class Solution:
    def restoreMatrix(self, rowSum, colSum):
        row = len(rowSum)
        col = len(colSum)
        
        res = [[0]*col for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                res[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= res[i][j]
                colSum[j] -= res[i][j]
        return res
                