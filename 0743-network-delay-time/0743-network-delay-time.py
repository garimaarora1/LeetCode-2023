class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        for i in range(n):
            for u,v,w in times:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        maxi = max(dist[1:])
        return maxi if maxi != float('inf') else -1
                    
        
            
            
            
        