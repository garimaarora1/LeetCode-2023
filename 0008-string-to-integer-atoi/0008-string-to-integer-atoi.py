class Solution:
    """
    Time complexity: O(N)

    We visit each character in the input at most once and for each character we spend     a constant amount of time.

    Space complexity: O(1)

    We have used only constant space to store the sign and the result.
    """
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        result = 0
        sign = 1
        
        while i < n and s[i] == ' ':
            i += 1
        
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            if result > (2 ** 31 - 1 - digit) // 10:
                return 2 ** 31 - 1 if sign == 1 else -2 ** 31
            
            result = result * 10 + digit
            i += 1
        return sign * result
