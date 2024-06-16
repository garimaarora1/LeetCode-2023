class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] *  numCourses
        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
            
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for adj in graph[node]:
                indegree[adj] -=1 
                if indegree[adj] == 0:
                    queue.append(adj)
            
        
        return count == numCourses