class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = maxi = nums[0]
        for num in nums[1:]:
            curr_sum = max(num, curr_sum+num)
            maxi = max(curr_sum, maxi)
        return maxi