class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_prefix = 0 
        for i in range(len(nums)):
            right_prefix = total_sum - left_prefix - nums[i]
            if right_prefix == left_prefix:
                return i
            left_prefix += nums[i]
        return -1
        