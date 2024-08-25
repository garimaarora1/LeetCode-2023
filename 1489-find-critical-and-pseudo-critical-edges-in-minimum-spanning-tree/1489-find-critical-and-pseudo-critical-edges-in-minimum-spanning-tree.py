class UnionFind:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        
        if x_parent != y_parent:
            if self.rank[x_parent] > self.rank[y_parent]:
                self.parent[y_parent] = x_parent
            elif self.rank[x_parent] < self.rank[y_parent]:
                self.parent[x_parent] = y_parent
            else:
                self.parent[x_parent] = y_parent
                self.rank[y_parent] += 1
            return True
        return False

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        uf = UnionFind(n)
        total_weight = 0
        total_edges = 0
        
        edges = [[weight, x, y, i] for i, (x, y, weight) in enumerate(edges)]
        
        edges.sort()
        
        for w, x, y, _ in edges:
            if uf.union(x, y):
                total_weight += w
                total_edges += 1
            if total_edges == n-1:
                break
        
        critical = []
        pseudo_critical = []
        
        for w, u, v, i in edges:
            uf_ignore = UnionFind(n)
            ignored_total_weight = 0
            ignored_total_edges = 0
            
            for ignore_w, x, y, j in edges:
                if i != j and uf_ignore.union(x, y):
                    ignored_total_weight += ignore_w
                    ignored_total_edges += 1
            
            if ignored_total_edges < n - 1 or ignored_total_weight > total_weight:
                critical.append(i)
                continue
            
            uf_force = UnionFind(n)
            force_weight = w
            uf_force.union(u, v)
            for w_force, x, y, j in edges:
                if i != j and uf_force.union(x, y):
                    force_weight += w_force
            
            if force_weight == total_weight:
                pseudo_critical.append(i)
        
        return [critical, pseudo_critical]
        
        
        