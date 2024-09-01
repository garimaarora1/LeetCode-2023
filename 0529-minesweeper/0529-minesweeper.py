class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) :
        """
        Time Complexity: 
        O(m×n)
        Space Complexity: 
        O(m×n)
        """
        m = len(board)
        if m == 0: 
            return board  
        n = len(board[0])

        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

        queue = deque([click]) 

        while queue:
            x, y = queue.popleft()

            if board[x][y] == 'M':
                board[x][y] = 'X'
                return board
            elif board[x][y] == 'E':
                mine_count = 0
                next_cells = deque()

                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy

                    if 0 <= new_x < m and 0 <= new_y < n:
                        if board[new_x][new_y] == 'M':
                            mine_count += 1
                        if board[new_x][new_y] == 'E':
                            next_cells.append((new_x, new_y))

                if mine_count == 0:
                    board[x][y] = 'B'
                    queue.extend(next_cells)
                else:
                    board[x][y] = str(mine_count)

        return board
