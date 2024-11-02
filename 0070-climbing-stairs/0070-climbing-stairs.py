class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        first = 1
        second = 2
        for i in range(3, n+1):
            temp = first + second
            first = second
            second = temp
        return second    
    