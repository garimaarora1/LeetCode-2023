class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(i, j):
            queue = deque()
            queue.append((i,j))
            while queue:
                x, y = queue.popleft()
                directions = [(0,-1), (0,1), (1,0), (-1,0)]
                for dr,dc in directions:
                    dx = x + dr
                    dy = y + dc
                    if 0<=dx<row and 0<=dy<col and grid[dx][dy] == '1' and (dx, dy) not in visited:
                        queue.append((dx, dy))
                        visited.add((dx, dy))
            
        row, col = len(grid), len(grid[0])
        visited = set()
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i,j) not in visited:
                    visited.add((i,j))
                    bfs(i,j)
                    count += 1
        return count
                    
    