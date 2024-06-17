class Solution:
    def left(self, nums, target, low, high):
        res = -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                res = mid
                high = mid -1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        print(11)
        return res
    
    def right(self, nums, target, low, high):
        res = -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                res = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return res

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return -1, -1

        l = self.left(nums, target, 0, len(nums)-1)
        r = self.right(nums, target, l, len(nums)-1)
        
        return l, r