class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        
        first = nums[0]
        second = max(first, nums[1])
        
        for i in range(2, n):
            temp = max(first + nums[i], second)
            first = second
            second = temp
        
        return second