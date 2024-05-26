class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable_index = 0
        for i in range(len(nums)):
            if max_reachable_index < i:
                return False
            max_reachable_index = max(max_reachable_index, i+nums[i])
        return True
        