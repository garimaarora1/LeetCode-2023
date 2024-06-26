class Solution:
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        parent = [i for i in range(row*col)]
        size = [1 for _ in range(row*col)] 
        found = False
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
                return parent[x]
            else:
                return x

        def union(x, y):
            x_parent, y_parent = find(x), find(y)
            if x_parent != y_parent:
                if size[x_parent] < size[y_parent]:
                    parent[x_parent] = y_parent
                    size[y_parent] += size[x_parent]
                else:
                    parent[y_parent] = x_parent
                    size[x_parent] += size[y_parent]
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    found = True
                    position_1 = i*col + j 
                    for dx, dy in directions:
                        x = i + dx
                        y = j + dy
                        if 0<=x<row and 0<=y<col and grid[x][y] == 1:
                            position_2 = x*col + y
                            union(position_2, position_1)         
        if found:
            return max(size)
        return 0