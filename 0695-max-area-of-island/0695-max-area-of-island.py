from typing import List

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        
        if rootP != rootQ:
            if self.size[rootP] > self.size[rootQ]:
                self.parent[rootQ] = rootP
                self.size[rootP] += self.size[rootQ]
            else:
                self.parent[rootP] = rootQ
                self.size[rootQ] += self.size[rootP]

    def getSize(self, p):
        rootP = self.find(p)
        return self.size[rootP]

class Solution:
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        uf = UnionFind(rows * cols)

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def getIndex(r, c):
            return r * cols + c

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            uf.union(getIndex(r, c), getIndex(nr, nc))

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, uf.getSize(getIndex(r, c)))

        return max_area