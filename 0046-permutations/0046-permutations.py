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
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i+1, curr_ans)
                nums[i], nums[j] = nums[j], nums[i]
        
        dfs(0, curr_ans)
        return ans