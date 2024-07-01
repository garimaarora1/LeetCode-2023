class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ones_count = 0 
        row = len(grid)
        col = len(grid[0])
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    ones_count += 1
        parent = [i for i in range(row*col)]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
                return parent[x]
            else:
                return x

        def union(x, y):
            x_parent, y_parent = find(x), find(y)
            if x_parent == y_parent:
                return False
            if x_parent < y_parent:
                parent[y_parent] = x_parent
            else:
                parent[x_parent] = y_parent
            return True
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    position_1 = i*col + j 
                    for dx, dy in directions:
                        x = i + dx
                        y = j + dy
                        if 0<=x<row and 0<=y<col and grid[x][y] == '1':
                            position_2 = x*col + y
                            if union(position_2, position_1):
                                ones_count -= 1
        return ones_count