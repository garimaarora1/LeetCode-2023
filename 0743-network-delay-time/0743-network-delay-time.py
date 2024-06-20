class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v, w))
            
        res = [float('inf')] * (n+1)
        res[k] = 0
        heap = []
        heapq.heappush(heap, (0,k))
        visited = set()
        while heap:
            dist, u = heapq.heappop(heap)
            if u not in visited:
                for v, w in graph[u]:

                    if res[v] > res[u] + w:
                        res[v] = res[u] + w
                        heapq.heappush(heap, (res[u]+w, v))
                visited.add(u)
                
        maxi = max(res[1:])
        return maxi if maxi != float('inf') else -1
                    

            
            
        