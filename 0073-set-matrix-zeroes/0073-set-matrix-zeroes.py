class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        is_row_zero = False
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0        
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        is_row_zero = True
        
        for i in range(1, row):
            for j in range(1, col):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
                    
        if matrix[0][0] == 0:
            for i in range(row):
                matrix[i][0] = 0
        
        if is_row_zero:
            for j in range(col):
                matrix[0][j] = 0
        
        