class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1 
        majority_element = nums[0]
        for i in range(1, len(nums)):
            if count == 0:
                majority_element = nums[i]
            count = count+1 if nums[i] == majority_element else count-1
        return majority_element
        
        
        