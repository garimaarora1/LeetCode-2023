class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        n = len(quiet)
        ans = [None] * n
        for u, v in richer:
            graph[v].append(u)
            
        
        def dfs(node):
            if ans[node] is None:
                ans[node] = node
                
                for child in graph[node]:
                    person = dfs(child)
                    if quiet[person] < quiet[ans[node]]:
                        ans[node] = person
            return ans[node]
                
        
        for i in range(n):
            dfs(i)
        return ans
            
        
        
        