class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        """
        1. sort nums, count = 0
        2. whenever nums[i-1] >= nums[i]:
        3. count += nums[i-1]-nums[i] + 1
        4. nums[i]= nums[i-1] + 1
        """
        
        nums.sort()
        count = 0
        
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                count += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1
        return count