class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr_ans = []
        n = len(nums)
        def dfs(i, curr_ans):
            if len(curr_ans) == n:
                ans.append(curr_ans.copy())
                return

            for j in range(i, n):
                curr_ans.append(nums[j])
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i+1, curr_ans)
                curr_ans.pop()
                nums[i], nums[j] = nums[j], nums[i]
        
        dfs(0, curr_ans)
        return ans