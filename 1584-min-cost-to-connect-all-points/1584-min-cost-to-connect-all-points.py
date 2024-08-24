class UnionFind:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.weight = [1] * n

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        
        if x_parent != y_parent:
            if self.weight[x_parent] < self.weight[y_parent]:
                self.parent[x_parent] = y_parent
                self.weight[y_parent] += self.weight[x_parent]
            else:
                self.parent[y_parent] = x_parent
                self.weight[x_parent] += self.weight[y_parent]
            return True
        return False

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)
        edges = []
        min_cost = 0
        total_edges = 0
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))
        
        edges.sort()
        for weight, i, j in edges:
            if uf.union(i, j):
                min_cost += weight
                total_edges += 1
            if total_edges == n - 1:
                break
        
        return min_cost
        
        
