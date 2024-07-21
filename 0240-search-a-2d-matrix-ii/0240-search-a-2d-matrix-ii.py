class Solution:        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        i = 0
        j = col - 1
        
        while i <= (row-1) and j >= 0:
            if matrix[i][j] == target:
                return True
            if target < matrix[i][j]:
                j -= 1
            else:
                i += 1
                
        return False
                
                
        
                
        