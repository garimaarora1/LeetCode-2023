class Solution:

    def reverse(self, nums, first, second):
        while first < second:
            nums[first], nums[second] = nums[second], nums[first]
            first += 1
            second -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0:
            return
        
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
        
        
        