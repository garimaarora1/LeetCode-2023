class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        ans = []
        def dfs(curr_ans): 
            if len(curr_ans) == len(nums):
                ans.append(curr_ans.copy())
                return
    
            for num in nums:
                if num not in curr_ans:
                    curr_ans.append(num)
                    dfs(curr_ans)
                    curr_ans.pop()
            
        
        dfs([])
        return ans
        