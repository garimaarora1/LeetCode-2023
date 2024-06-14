class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # construct graph
        graph = defaultdict(list)
        
        n = len(bombs)
        max_connected_components = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                # add j to i's adj list if i can detonate j
                
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]
                
                if ri ** 2 >= (xi-xj)**2 + (yi-yj)**2:
                    graph[i].append(j)
        
        def bfs(node):
            queue = deque()
            visited = set()
            queue.append(node)
            visited.add(node)
            while queue:
                node = queue.popleft()
                for adj in graph[node]:
                    if adj not in visited:
                        queue.append(adj)
                        visited.add(adj)
            return len(visited)
        
        
        
        for i in range(n):
            curr_connected_components = bfs(i)
            max_connected_components = max(max_connected_components, curr_connected_components)
        return max_connected_components
        
        
        # bfs