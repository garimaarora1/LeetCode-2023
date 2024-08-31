class UnionFind:
    
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if x == self.parents[x]:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        
        if x_parent != y_parent:
            if self.rank[x_parent] < self.rank[y_parent]:
                self.parents[x_parent] = y_parent
            elif self.rank[x_parent] > self.rank[y_parent]:
                self.parents[y_parent] = x_parent
            else:
                self.parents[y_parent] = x_parent
                self.rank[x_parent] += 1
            return True
        return False

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        connected_components = n

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1 and uf.union(i, j):
                    connected_components -= 1
        return connected_components
        