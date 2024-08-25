class UnionFind:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        
        if x_parent != y_parent:
            if self.rank[x_parent] < self.rank[y_parent]:
                self.parent[x_parent] = y_parent
            elif self.rank[x_parent] > self.rank[y_parent]:
                self.parent[y_parent] = x_parent
            else:
                self.parent[y_parent] = x_parent
                self.rank[x_parent] += 1
            return True
        return False

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        components = 0
        n = row * col
        uf = UnionFind(n)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1': 
                    components += 1
                    pos1 = i * col + j
                    
                    for dr, dc in directions:
                        dx = i + dr
                        dy = j + dc
                        
                        pos2 = dx * col + dy
                        
                        if 0<=dx<row and 0<=dy<col and grid[dx][dy] == '1' and uf.union(pos1, pos2):
                            components -= 1
        return components