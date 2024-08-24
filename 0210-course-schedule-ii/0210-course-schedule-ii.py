class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degrees = [0] * numCourses
        queue = deque()
        count = 0
        res = []

        for u, v in prerequisites:
            graph[v].append(u)
            in_degrees[u] += 1
        
        for i, val in enumerate(in_degrees):
            if val == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            res.append(node)
            count += 1
    
            for adj in graph[node]:
                in_degrees[adj] -= 1
                if in_degrees[adj] == 0:
                    queue.append(adj)
        
        return res if numCourses == count else []
        
        