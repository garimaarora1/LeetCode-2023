class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        res = []
        
        def backtrack(node, path):
            if node == target:
                res.append(path.copy())
                return
            
            for neighbour in graph[node]:
                path.append(neighbour)
                backtrack(neighbour, path)
                path.pop()
        backtrack(0, [0])
        return res