class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 2, x//2
        while left <= right:
            mid = left + (right-left)//2
            sq = mid * mid
            if sq == x:
                return mid
            elif sq < x:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1
        