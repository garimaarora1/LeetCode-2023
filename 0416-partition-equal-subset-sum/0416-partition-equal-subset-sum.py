class Solution(object):
    def canPartition(self, nums):
        n = len(nums)
        if n == 0:
            return True
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [[-1] * (target + 1) for _ in range(n)]
        
        def dfs(i, target):
            if target == 0:
                return True
            if i == n:
                return False
            if dp[i][target] != -1:
                return dp[i][target]
            
            if target - nums[i] >= 0:
                dp[i][target] = dfs(i + 1, target - nums[i]) or dfs(i + 1, target)
            else:
                dp[i][target] = dfs(i + 1, target)
            
            return dp[i][target]
        
        return dfs(0, target)
