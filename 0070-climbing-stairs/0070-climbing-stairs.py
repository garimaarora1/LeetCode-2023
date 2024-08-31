class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        start = 1
        second = 2
        for i in range(3, n+1):
            temp = start + second
            start = second
            second = temp
        return second
            