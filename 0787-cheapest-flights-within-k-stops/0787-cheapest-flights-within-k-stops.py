class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        
        for u, v, price in flights:
            graph[u].append((v, price))
        
        queue = deque()
        # price to visit each node
        prices = [float('inf')]*n
        prices[src] = 0
        # price, source, steps
        queue.append((0, src, 0))
        
        while queue:
            price, node, steps = queue.popleft()

            for adj_node, adj_price in graph[node]:
                new_price = adj_price+price
                if steps <= k and prices[adj_node] > new_price:
                    prices[adj_node] = new_price
                    queue.append((new_price, adj_node, steps+1))
        return prices[dst] if prices[dst] != float('inf') else -1
        