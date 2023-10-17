class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        x_abs = abs(x)
        limit = [-2**31, 2**31 - 1]
        
        while x_abs:
            modulo = x_abs % 10

            result = result * 10 + modulo
            x_abs = x_abs // 10
        
        if x < 0:
            result = -result
        
        if result < limit[0] or result > limit[1]:
            return 0
        return result
        