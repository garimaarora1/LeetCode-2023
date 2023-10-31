class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        n = len(nums)
        right = n - 1
        result = [0] * n
        for i in range(n - 1, -1, -1):
            right_val = abs(nums[right])
            left_val = abs(nums[left])
            if right_val > left_val:
                val = right_val
                right -= 1
            else:
                val = left_val
                left += 1
            result[i] = val**2
        return result