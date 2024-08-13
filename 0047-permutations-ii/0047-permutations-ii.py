from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr_ans = []
        n = len(nums)
        nums.sort()
        
        def dfs(used):
            if len(curr_ans) == n:
                ans.append(list(curr_ans))
                return
            
            for j in range(n):
                if used[j] or (j > 0 and nums[j] == nums[j-1] and not used[j-1]):
                    continue
                
                curr_ans.append(nums[j])
                used[j] = True
                dfs(used)
                used[j] = False
                curr_ans.pop()

        dfs([False] * n)
        return ans
