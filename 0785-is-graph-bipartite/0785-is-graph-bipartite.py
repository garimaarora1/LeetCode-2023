class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0]*len(graph)
        
        def bfs(i):
            if visited[i]:
                return True
            queue = deque()
            queue.append(i)
            visited[i] = -1
            while queue:
                i = queue.popleft()
                for adj in graph[i]:
                    if visited[adj] == visited[i]:
                        return False
                    elif not visited[adj]:
                        queue.append(adj)
                        visited[adj] = -1 * visited[i]
            return True

        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True