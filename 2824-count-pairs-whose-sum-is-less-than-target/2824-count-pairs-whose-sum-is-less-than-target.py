class Solution(object):
    def countPairs(self, nums, target):
        nums.sort()
        n = len(nums)
        left, right = 0, n - 1
        count = 0

        while left < right:
            if nums[left] + nums[right] < target:
                count += (right - left)  # all pairs with left and right
                left += 1
            else:
                right -= 1

        return count