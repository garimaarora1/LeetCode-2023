class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high-low) // 2
            if ((mid-1) < 0 or nums[mid-1] > nums[mid]) and (mid+1 == len(nums) or nums[mid] < nums[mid+1]):
                return nums[mid]
            if nums[mid] < nums[high]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
        
        
        