class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1 pointer: to point to zero element
        # 2 pointer: to point to non-zero element
        # increment the zero element pointer whenever a non-zero element is found
        
        j = 0 
        for i in range(len(nums)):
            if nums[i] != 0:
                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1