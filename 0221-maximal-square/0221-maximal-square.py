class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        # (r, c): max length
        cache = {} 

        def helper(r, c):
            if r >= row or c >= col:
                return 0
            
            if (r, c) in cache:
                return cache[(r, c)]
            down = helper(r+1, c)
            right = helper(r, c+1)
            diagonal = helper(r+1, c+1)

            cache[(r, c)] = 0
            if matrix[r][c] == '1':
                cache[(r, c)] = 1 + min(right, down, diagonal)
            
            return cache[(r, c)]
        
        helper(0, 0)
        return max(cache.values()) ** 2