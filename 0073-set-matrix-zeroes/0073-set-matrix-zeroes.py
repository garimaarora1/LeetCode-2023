class Solution:
    def setZeroes(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_row_zero, is_col_zero = False, False
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] == 0:
                    a[i][0], a[0][j] = 0, 0
                    if i == 0:
                        is_row_zero = True
                    if j == 0:
                        is_col_zero = True
        for i in range(1, len(a)):
            for j in range(1, len(a[0])):
                if a[0][j] == 0 or a[i][0] == 0:
                    a[i][j] = 0
        if is_row_zero:
            for j in range(len(a[0])):
                a[0][j] = 0
        if is_col_zero:
            for i in range(len(a)):
                a[i][0] = 0
                