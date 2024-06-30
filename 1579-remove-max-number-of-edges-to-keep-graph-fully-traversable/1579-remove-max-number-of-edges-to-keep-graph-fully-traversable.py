class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        #    int find(int u) {
        # if (u != parent[u])
        #     parent[u] = find(parent[u]);
        # return parent[u];
        def find(x, parent):
            if parent[x] != x:
                parent[x] = find(parent[x], parent)
            return parent[x]
                
                # return find(parent[x], parent)
        
        def union(u, v, parent):
            rep_u = find(u, parent)
            rep_v = find(v, parent)
            if rep_u != rep_v:
                if rep_u > rep_v:
                    parent[rep_v] = rep_u
                else:
                    parent[rep_u] = rep_v
                return True
            return False
        
        
        edges = sorted(edges, key=lambda x:-x[0])
        alice_parents = [i for i in range(n+1)]
        bob_parents = [i for i in range(n+1)]
        alice_count, bob_count = 0, 0
        for typ, u, v in edges:
            if typ == 3:
                if not union(u, v, alice_parents):
                    alice_count += 1
                union(u, v, bob_parents)
            elif typ == 2:
                if not union(u, v, bob_parents):
                    bob_count += 1
            else:
                if not union(u, v, alice_parents):
                    alice_count += 1

        count = 0
        for i in range(1, len(alice_parents)):
            if i == alice_parents[i]:
                count += 1
            if count == 2:
                return -1
        count = 0
        for i in range(1, len(bob_parents)):
            if i == bob_parents[i]:
                count += 1
            if count == 2:
                return -1
        return alice_count + bob_count
        
                
                
            
            
                