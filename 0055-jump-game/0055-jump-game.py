class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        for i in range(len(nums)):
            if max_reachable < i: 
                return False
            max_reachable = max(max_reachable, nums[i]+i)   
        return True