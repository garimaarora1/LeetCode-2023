class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        i,j = 2, x//2
        while i<=j:
            mid = i + (j-i)//2
            sq = mid * mid
            if sq == x:
                return mid
            elif sq < x:
                i = mid + 1
            else:
                j = mid - 1
        return i - 1