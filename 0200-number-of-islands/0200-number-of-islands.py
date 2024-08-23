class UnionFind:
    def __init__(self, row, col):
        self.parents = [i for i in range(row*col)]

    def find(self, x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        
        if parent_x != parent_y:
            if parent_x < parent_y:
                self.parents[parent_y] = parent_x
            else:
                self.parents[parent_x] = parent_y
            
            return True
        return False

class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        count = 0
        uf = UnionFind(row, col)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    count += 1
                    pos1 = i * col + j
                    
                    for dx, dy in directions:
                        dr = i + dx
                        dc = j + dy
                        if 0<=dr<row and 0<=dc<col and grid[dr][dc] == '1':
                            pos2 = dr * col + dc
                            if uf.union(pos1, pos2):
                                count -= 1
        return count
                                
                        
                        
                        
                        