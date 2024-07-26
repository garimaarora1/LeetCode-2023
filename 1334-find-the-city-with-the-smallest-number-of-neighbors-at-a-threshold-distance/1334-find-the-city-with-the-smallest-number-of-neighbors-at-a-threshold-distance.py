class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[0]*n for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    graph[i][j] = float('inf')

        for u,v,w in edges:
            graph[u][v] = w
            graph[v][u] = w
            
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        value = float('inf')
        mini_node = -1
        for i in range(n):
            curr_value = 0
            for j in range(n):
                if graph[i][j] <= distanceThreshold:
                    curr_value += 1
            if curr_value <= value:
                value = curr_value
                mini_node = i
        return mini_node
    
    
    
    
            
                    
        
        
        