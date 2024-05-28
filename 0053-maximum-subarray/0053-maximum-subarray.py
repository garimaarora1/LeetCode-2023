class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_array_sum = curr_max = nums[0]
        for num in nums[1:]:
            curr_max = max(curr_max+num, num)
            max_sub_array_sum = max(max_sub_array_sum, curr_max)
        return max_sub_array_sum
        
        