class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        maxi_sum = maxi
        for num in nums[1:]:
            maxi = max(maxi+num, num)
            maxi_sum = max(maxi_sum, maxi)
        return maxi_sum
            