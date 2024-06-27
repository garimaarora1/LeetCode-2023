class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        
        def bfs(i,j):
            queue = deque()
            queue.append((i,j))
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            curr_area = 1
            while queue:
                dx, dy = queue.pop()
                for dr, dc in directions:
                    x = dx + dr
                    y = dy + dc
                    if 0<=x<rows and 0<=y<cols and grid[x][y] == 1 and (x,y) not in visited:
                        visited.add((x,y))
                        queue.append((x,y))
                        curr_area += 1
            return curr_area
                           
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    visited.add((i,j))
                    curr_area = bfs(i,j)
                    max_area = max(max_area, curr_area)
        return max_area
        