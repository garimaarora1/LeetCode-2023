class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.fun(nums, 0, len(nums)-1, target)
    
    def fun(self, nums, low, high, target):
        if low > high:
            return -1
        mid = (low + high)//2

        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            return self.fun(nums, low, mid-1, target)
        else:
            return self.fun(nums, mid+1, high, target)