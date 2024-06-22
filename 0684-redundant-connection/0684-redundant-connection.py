class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(1001)]
        
        def find(x):
            
            if parent[x] != x:
                return find(parent[x])
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
    
        for x,y in edges:
            if not union(x, y):
                return [x,y]
        
        
        
        