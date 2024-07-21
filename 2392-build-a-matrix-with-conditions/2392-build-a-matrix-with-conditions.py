class Solution:
    
    def topo_sort(self, edges, n):
        graph = defaultdict(list)
        in_degree = [0] * (n+1)
        order = []
        for u,v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        queue = deque()
        for i in range(1, n+1):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            num = queue.popleft()
            n -= 1
            order.append(num)
            for adj in graph[num]:
                in_degree[adj] -= 1
                if in_degree[adj] == 0:
                    queue.append(adj)
                    
        if n != 0:
            return []
        return order

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        row_result = self.topo_sort(rowConditions, k)
        col_result = self.topo_sort(colConditions, k)
        res = [[0] * k for _ in range(k)]
        if not row_result or not col_result:
            return []
        
        for i in range(k):
            for j in range(k):
                if row_result[i] == col_result[j]:
                    res[i][j] = row_result[i]
        return res