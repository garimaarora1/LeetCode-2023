class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            while queue:
                x, y = queue.popleft()
                for dr, dc in directions:
                    dx = x + dr
                    dy = y + dc
                    if 0<=dx<rows and 0<=dy<cols and grid[dx][dy] == '1' and (dx, dy) not in visited:
                        visited.add((dx, dy))
                        queue.append((dx, dy))
        
        visited = set()
        count = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count += 1
                    bfs(i, j)
                    visited.add((i, j))
        return count