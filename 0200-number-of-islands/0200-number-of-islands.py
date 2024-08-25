class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            
            while queue:
                i, j = queue.popleft()
                for dr, dc in directions:
                    dx = i + dr
                    dy = j + dc
                    if 0<=dx<row and 0<=dy<col and grid[dx][dy] == '1' and (dx, dy) not in visited:
                        visited.add((dx, dy))
                        queue.append((dx, dy))
            
        row = len(grid)
        col = len(grid[0])
        visited = set()
        components = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i, j) not in visited:
                    visited.add((i, j))
                    bfs(i, j)
                    components += 1
                    
        return components