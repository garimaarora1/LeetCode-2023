class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_mini = []
        col_maxi = []
        res = []
        for mat in matrix:
            row_mini.append(min(mat))

        for j in range(len(matrix[0])):
            maxi = []
            for i in range(len(matrix)):
                maxi.append(matrix[i][j])
            col_maxi.append(max(maxi))
            
        for val in row_mini:
            if val in col_maxi:
                res.append(val)
        return res