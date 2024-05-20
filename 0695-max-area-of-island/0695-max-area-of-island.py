class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def bfs(i,j):
            queue = deque()
            queue.append((i,j))
            visited.add((i,j))
            count = 0
            directions = [(0,-1),(0,1),(1,0),(-1,0)]
            while queue:
                r,c = queue.popleft()
                count += 1
                for x,y in directions:
                    dx = x+r
                    dy = y+c
                    if 0<=dx<row and 0<=dy<col and grid[dx][dy] == 1 and (dx,dy) not in visited:
                        visited.add((dx,dy))
                        queue.append((dx,dy))
                
            return count  
                
        row, col = len(grid), len(grid[0])
        visited = set()
        maxi = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in visited:
                    count = bfs(i,j)
                    maxi = max(maxi, count)
        return maxi