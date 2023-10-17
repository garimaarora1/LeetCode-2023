class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        def transpose():
            for i in range(n):
                for j in range(i+1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        def reverse_row():
            for i in range(n):
                start, end = 0, n-1
                while start < end:
                    matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
                    start += 1
                    end -= 1
        transpose()
        reverse_row()