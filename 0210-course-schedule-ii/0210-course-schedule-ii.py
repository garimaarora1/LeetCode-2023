class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
            
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        res = []
        
        while queue:
            node = queue.popleft()
            res.append(node)
            for adj in graph[node]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    queue.append(adj)
        
        if len(res) == numCourses:
            return res
        print(res)
        return []
            
        