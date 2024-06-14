class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # construct graph
        graph = defaultdict(list)
        
        n = len(bombs)
        max_connected = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]

                # add j to i's adj list if i can detonate j
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
            curr_connected = bfs(i)
            max_connected = max(max_connected, curr_connected)
        return max_connected