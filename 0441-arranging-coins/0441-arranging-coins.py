class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = left + (right-left) // 2
            coins_in_mid_row = (mid * (mid+1)) // 2
            if coins_in_mid_row == n:
                return mid 
            elif coins_in_mid_row < n:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1
        # or return right