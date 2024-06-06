class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(i,j):
            queue = deque()
            queue.append((i,j))
            directions = ((0,1),(1,0),(0,-1),(-1,0))
            curr_count = 0
            while queue:
                x, y = queue.popleft()
                for dr, dc in directions:
                    dx = x + dr
                    dy = y + dc
                    
                    if 0<=dx<row and 0<=dy<col and grid[dx][dy] == 1 and (dx, dy) not in visited:
                        curr_count += 1
                        visited.add((dx, dy))
                        queue.append((dx, dy))
            return curr_count


        visited = set()
        row = len(grid)
        col = len(grid[0])
        res = 0
        for i in range(row):
            for j in range(col):
                count = 0
                if grid[i][j] == 1 and grid[i][j] not in visited:
                    count += 1
                    visited.add((i,j))
                    count += bfs(i,j)
                    res = max(res, count)
        return res
        
        
        