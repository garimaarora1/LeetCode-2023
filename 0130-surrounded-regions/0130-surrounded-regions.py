class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        
        def bfs(x, y):
            queue = deque()
            queue.append((i,j))
            visited.add((i,j))
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            while queue:
                x, y = queue.popleft()
                for dr, dc in directions:
                    dx, dy = x+dr, y+dc
                    if 0<=dx<row and 0<=dy<col and (dx, dy) not in visited and board[dx][dy] == 'O':
                        queue.append((dx, dy))
                        visited.add((dx,dy))

        visited = set()
        
        for i in range(row):
            for j in range(col):
                if i == 0 or i == row-1 or j == 0 or j == col-1:
                    if board[i][j] == 'O' and (i,j) not in visited:
                        bfs(i, j)
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O' and (i,j) not in visited:
                    board[i][j] = 'X'
