class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        
        for u, v, price in flights:
            graph[u].append((v, price))
        
        heap = []
        # price to visit each node
        prices = defaultdict(lambda: float('inf'))
        prices[(src, 0)] = 0
        # price, source, steps
        heap.append((0, src, 0))
        
        while heap:
            price, node, steps = heapq.heappop(heap)
            
            if node == dst:
                return price
            if steps <= k:
                for adj_node, adj_price in graph[node]:
                    new_price = adj_price+price
                    if new_price < prices.get((adj_node, steps + 1), float('inf')):
                        prices[(adj_node, steps + 1)] = new_price
                        heapq.heappush(heap, (new_price, adj_node, steps+1))
        return -1
                
                
        
        