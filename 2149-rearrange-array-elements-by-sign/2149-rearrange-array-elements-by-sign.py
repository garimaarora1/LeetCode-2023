class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)
        
        i = 0
        j = 0
        while i < len(nums):
            nums[i] = positives[j]
            i += 1
            nums[i] = negatives[j]
            j += 1
            i += 1
        
        return nums