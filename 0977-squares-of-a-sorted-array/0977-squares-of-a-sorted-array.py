class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        n = len(nums)
        right = n - 1
        result = [0] * n
        i = n - 1
        while left <= right:
            right_val = abs(nums[right])
            left_val = abs(nums[left])
            if right_val > left_val:
                result[i] = right_val**2
                right -= 1
            else:
                result[i] = left_val**2
                left += 1
            i -= 1
        return result