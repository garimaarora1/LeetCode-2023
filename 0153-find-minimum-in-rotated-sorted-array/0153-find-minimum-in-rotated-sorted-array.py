class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end-start) // 2
            if ((mid - 1) < 0 or nums[mid-1] > nums[mid]) and (mid+1 == len(nums) or nums[mid] < nums[mid+1]):
                return nums[mid]
            elif nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        return -1
         