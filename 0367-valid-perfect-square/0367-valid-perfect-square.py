class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0 
        right = num
        while left <= right:
            mid = left + (right - left) // 2
            sq = mid*mid
            if sq == num:
                return True
            elif sq < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
   