class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
    
        def dfs(node, parent):
            nonlocal min_total_fuel
            
            passengers = 0
            
            for adj in graph[node]:
                if adj != parent:
                    p = dfs(adj, node)
                    passengers += p
                    min_total_fuel += ceil(p/seats)
            return passengers + 1
        
        min_total_fuel = 0
        dfs(0, -1)
        return min_total_fuel
        
        