class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        courses: 0 n-1
        1 -> 0
        """
        graph = defaultdict(list)
        in_degrees = [0] * numCourses
        queue = deque()
        count = 0

        for u, v in prerequisites:
            graph[v].append(u)
            in_degrees[u] += 1
        
        for i, val in enumerate(in_degrees):
            if val == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            count += 1
            for adj in graph[node]:
                in_degrees[adj] -= 1
                if in_degrees[adj] == 0:
                    queue.append(adj)
        
        return count == numCourses
        
        