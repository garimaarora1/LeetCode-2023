class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        x_abs = abs(x)
        lower_limit = -2**31
        upper_limit = 2**31 - 1
        
        while x_abs:
            modulo = x_abs % 10

            result = result * 10 + modulo
            x_abs = x_abs // 10
        
        if x < 0:
            result = -result
        
        if result < lower_limit or result > upper_limit:
            return 0
        return result
        