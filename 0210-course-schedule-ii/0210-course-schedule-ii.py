class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        queue = deque()
        count = 0
        res = []

        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1
            
        for i, val in enumerate(in_degree):
            if val == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            count += 1
            res.append(node)

            for adj in graph[node]:
                in_degree[adj] -= 1
                if in_degree[adj] == 0:
                    queue.append(adj)

        return res if count == numCourses else []
                    