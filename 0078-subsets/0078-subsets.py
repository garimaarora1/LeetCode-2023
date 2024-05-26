class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 1. order has to be maintained 
        # 2. total 2**n -1
        # 3. TC: 2**n
        def dfs(idx, path):
            if idx == len(nums):
                res.append(path.copy())
                return
            path.append(nums[idx])
            dfs(idx+1, path)
            path.pop()
            
            dfs(idx+1, path)
            
        res = []
        path = []
        dfs(0, path)
        return res