class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        remaining_nodes = n
        
        
        curr_nodes = 0
        unreachable_pairs = 0
        
        def bfs(node):
            queue = deque()
            size = 1
            queue.append(node)
            visited.add(node)
            while queue:
                node = queue.popleft()
                for adj in graph[node]:
                    if adj not in visited:
                        size += 1
                        queue.append(adj)
                        visited.add(adj)
            return size

        visited = set()    

        for i in range(n):
            if i not in visited:
                curr_nodes = bfs(i)
                remaining_nodes -= curr_nodes
                unreachable_pairs += curr_nodes * remaining_nodes
        
        return unreachable_pairs
                
        