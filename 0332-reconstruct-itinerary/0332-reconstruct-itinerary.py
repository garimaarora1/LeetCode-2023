class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = defaultdict(list)
        for u, v in tickets:
            graph[u].append(v)
        
        res =  []
        def dfs(source):
            while graph[source]:
                node = graph[source].pop(0)
                dfs(node)
            res.append(source)
                
        source = "JFK"
        dfs(source)
        return res[::-1]
    
    [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]