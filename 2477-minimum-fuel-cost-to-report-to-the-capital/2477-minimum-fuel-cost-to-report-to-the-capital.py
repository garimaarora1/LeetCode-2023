class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:

        graph = defaultdict(list)
        for u,v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, k, parent):
            # if len(graph[node]) == 1 and graph[node] == parent:
            #     return (1,0)
            
            total_count = 0
            total_fuel = 0
            for adj in graph[node]:
                if adj != parent:
                    node_count, fuel = dfs(adj, k, node)
                    total_count += node_count
                    total_fuel += fuel + ceil((node_count)/k)  
            return total_count+1, total_fuel
        
        _, fuel = dfs(0, seats, -1)
        return fuel
        