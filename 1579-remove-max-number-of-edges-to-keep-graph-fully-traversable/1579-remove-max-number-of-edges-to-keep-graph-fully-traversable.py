class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(x, parent):
            if parent[x] != x:
                parent[x] = find(parent[x], parent)
            return parent[x]

        def union(x, y, parent, rank):
            parent_x = find(x, parent)
            parent_y = find(y, parent)
            if parent_x != parent_y:
                if rank[parent_x] > rank[parent_y]:
                    parent[parent_y] = parent_x
                elif rank[parent_x] < rank[parent_y]:
                    parent[parent_x] = parent_y
                else:
                    parent[parent_x] = parent_y
                    rank[parent_y] += 1
                return True
            return False
        
        a_count = 1
        b_count = 1
        redundant_edges = 0
        a_parent = [i for i in range(n+1)]
        a_rank = [1 for _ in range(n+1)]
        b_parent = [i for i in range(n+1)]
        b_rank = [1 for _ in range(n+1)]
        edges = sorted(edges, key=lambda x:-x[0])
        
        for typ,u,v in edges:
            if typ == 3:
                if union(u, v, a_parent, a_rank):
                    a_count += 1
                    b_count += 1
                else:
                    redundant_edges += 1
                union(u,v, b_parent, b_rank)
            elif typ == 2:
                if union(u, v, b_parent, b_rank):
                    b_count += 1
                else:
                    redundant_edges += 1
            else:
                if union(u, v, a_parent, a_rank):
                    a_count += 1
                else:
                    redundant_edges += 1

        if a_count < n or b_count < n:
            return - 1
        return redundant_edges
 