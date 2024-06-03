class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            queue = deque()
            queue.append((i,j))
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            while queue:
                x, y = queue.popleft()
                for dr, dc in directions:
                    dx = x + dr
                    dy = y + dc
                    if 0<=dx<row and 0<=dy<col and grid[dx][dy] == '1' and (dx, dy) not in visited:
                        visited.add((dx, dy))
                        queue.append((dx, dy))
                    
        row = len(grid)
        col = len(grid[0])
        visited = set()
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i,j) not in visited:
                    visited.add((i,j))
                    bfs(i, j)
                    count += 1
        return count
                    
        