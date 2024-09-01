class UnionFind:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x]) # path compression
        return self.parent[x]
    
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        
        if parent_x != parent_y:
            if self.rank[parent_x] < self.rank[parent_y]:
                self.parent[parent_x] = parent_y
            elif self.rank[parent_x] > self.rank[parent_y]:
                self.parent[parent_y] = parent_x
            else:
                self.parent[parent_y] = parent_x
                self.rank[parent_x] += 1
            return True
        return False

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        n = row * col
        uf = UnionFind(n)
        count = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    count += 1
                    pos1 = i * col + j
                
                    for dx, dy in directions:
                        x = i + dx
                        y = j + dy
                        
                        if 0<=x<row and 0<=y<col and grid[x][y] == '1':
                            pos2 = x * col + y
                            
                            if uf.union(pos1, pos2):
                                count -= 1
        return count
        
        