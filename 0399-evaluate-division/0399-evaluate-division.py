class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        res = []
        for i,equation in enumerate(equations):
            var1, var2 = equation[0], equation[1]
            value = values[i]
            
            graph[var1].append((value, var2))
            graph[var2].append((1/value, var1))
        def bfs(var1):
            visited = set()
            queue = deque()
            queue.append((1, var1))
            while queue:
                curr_product, var = queue.popleft()
                if var == var2:
                    return curr_product
                visited.add(var)
                for value, adj in graph[var]:
                    if adj not in visited:
                        queue.append((curr_product*value, adj))
            return -1.0

        for query in queries:
            var1, var2 = query[0], query[1]
            if var1 not in graph or var2 not in graph:
                res.append(-1)
                continue
            res.append(bfs(var1))
        return res
        