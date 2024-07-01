class Solution:
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ones_count = 0 
        row = len(grid)
        col = len(grid[0])
        max_count = 0
        parent = [i for i in range(row*col)]
        size = [1 for _ in range(row*col)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
                return parent[x]
            else:
                return x

        def union(x, y):
            nonlocal max_count
            x_parent, y_parent = find(x), find(y)
            if x_parent == y_parent:
                return False
            if size[x_parent] < size[y_parent]:
                parent[x_parent] = y_parent
                size[y_parent] += size[x_parent]
            else:
                parent[y_parent] = x_parent
                size[x_parent] += size[y_parent]
            curr_max = max(size[x_parent], size[y_parent])
            max_count = max(max_count, curr_max)
            return True
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    position_1 = i*col + j 
                    for dx, dy in directions:
                        x = i + dx
                        y = j + dy
                        if 0<=x<row and 0<=y<col and grid[x][y] == 1:
                            position_2 = x*col + y
                            union(position_2, position_1)
        max_area = 0
        found = False
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    found = True
        if found:
            return max(size)
        return 0