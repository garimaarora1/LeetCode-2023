class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        # def find(x, parent):
        #     if parent[x] == x:
        #         return x
        #     else:
        #         temp_parent = find(parent[x], parent)
        #         parent[x] = temp_parent
        #         return temp_parent
        
        def find(x, parent):
            if parent[x] != x:
                parent[x] = find(parent[x], parent)
            return parent[x]

        def union(x, y, parent):
            parent_x = find(x, parent)
            parent_y = find(y, parent)
            if parent_x != parent_y:
                if parent_x < parent_y:
                    parent[parent_y] = parent_x
                else:
                    parent[parent_x] = parent_y
                return True
            
            return False
        
        a_count = 0
        b_count = 0
        a_parent = [i for i in range(n+1)]
        b_parent = [i for i in range(n+1)]
        edges = sorted(edges, key=lambda x:-x[0])
        
        for typ,u,v in edges:
            if typ == 3:
                if not union(u, v, a_parent):
                    a_count += 1
                union(u,v, b_parent)
            elif typ == 2:
                if not union(u, v, b_parent):
                    b_count += 1
            else:
                if not union(u, v, a_parent):
                    a_count += 1

        count = 0
        for i in range(1, len(a_parent)):
            if i == a_parent[i]:
                count += 1
            if count == 2:
                return -1
        count = 0
        for i in range(1, len(b_parent)):
            if i == b_parent[i]:
                count += 1
            if count == 2:
                return -1
        
        return a_count + b_count
        
        
            
                    