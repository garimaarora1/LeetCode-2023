class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curr_subset = []
        def dfs(i, curr_subset):
            if len(curr_subset) == k:
                res.append(curr_subset.copy())
                return
            
            for j in range(i, n+1):
                curr_subset.append(j)
                dfs(j+1, curr_subset)
                curr_subset.pop()
        
        dfs(1, curr_subset)
        return res