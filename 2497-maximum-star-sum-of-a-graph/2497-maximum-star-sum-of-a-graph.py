class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], K: int) -> int:
        if not edges:
            return max(vals)
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        max_sum = max(vals)
        
        for key, nodes in graph.items():
            curr_sum = vals[key]
            min_heap = []
            for node in nodes:
                neighbor_value = vals[node]
                if neighbor_value > 0:
                    heapq.heappush(min_heap, neighbor_value)
                    if len(min_heap) > K:
                        heapq.heappop(min_heap)
            
            curr_sum += sum(min_heap)
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
