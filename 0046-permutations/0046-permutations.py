class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr_ans = []
        n = len(nums)
        def dfs(i, curr_ans):
            if i == n:
                ans.append(nums.copy())
                return

            for j in range(i, n):
                # curr_ans.append(nums[j])
                # important
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i+1, curr_ans)
                # curr_ans.pop()
                # important
                nums[i], nums[j] = nums[j], nums[i]
        
        dfs(0, curr_ans)
        return ans
    
# res = [[1, 2, 3], ]         BT

# nums = [1, 2, 3]
#     | dfs(3, [1, 2, 3]) 3, [1, 2, 3]    | 
#     | dfs(2, [1, 2]) 2, [1, 2, 3]       | [1, 2]
#     | dfs(1, [1]) j: 1, [1, 2]          | [1]  i:1  j: 2 [1, 3] nums = [1, 3, 2]
#     | dfs(0, []): j: 0, [1]             |
    
    