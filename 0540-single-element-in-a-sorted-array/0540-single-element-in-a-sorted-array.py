class Solution(object):
    def singleNonDuplicate(self, nums):
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low + high) // 2
            
            if (mid-1 < 0 or nums[mid-1] != nums[mid]) and \
                (mid+1 == len(nums) or nums[mid+1] != nums[mid]):
                return nums[mid]
            leftsize = mid-1 if nums[mid-1] == nums[mid] else mid

            if leftsize % 2 == 0:
                low = mid + 1
            else:
                high = mid - 1

        return -1