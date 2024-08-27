class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),         (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0

                for dr, dc in directions:
                    rr, cc = r + dr, c + dc

                    if (0 <= rr < rows) and (0 <= cc < cols) and abs(board[rr][cc]) == 1:
                        live_neighbors += 1

                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = -1  
                else:
                    if live_neighbors == 3:
                        board[r][c] = 2  

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == -1:
                    board[r][c] = 0
                elif board[r][c] == 2:
                    board[r][c] = 1

