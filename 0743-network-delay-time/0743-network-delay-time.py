class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = [float('inf')] * (n+1)
        d[k] = 0
        for i in range(n):
            for u,v,w in times:
                if d[u] != float('inf') and d[u] + w < d[v]:
                    d[v] = d[u] + w
        maxi = max(d[1:])
        return maxi if maxi != float('inf') else -1
                    
        
            
            
            
        