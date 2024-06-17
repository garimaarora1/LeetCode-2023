class Solution:
    def binarySearch(self, nums, target, low, high, is_left):
        res = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                res = mid
                if is_left:
                    high = mid -1
                else:
                    low = mid +1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return res
    

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return -1, -1

        l = self.binarySearch(nums, target, 0, len(nums)-1, True)
        r = self.binarySearch(nums, target, l, len(nums)-1, False)
        
        return l, r