class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr_ans = []
        n = len(nums)
        def dfs(i, curr_ans):
            ans.append(curr_ans.copy())
            
            for j in range(i, n):
                curr_ans.append(nums[j])
                dfs(j+1, curr_ans)
                curr_ans.pop()
        dfs(0, curr_ans)
        
        return ans
        
        