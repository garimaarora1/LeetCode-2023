class Solution:
    def get_next_number(self, n):
        total_sum = 0
        while n > 0:
            last_digit = n % 10
            n = n // 10
            total_sum += last_digit**2
        return total_sum
        
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            n = self.get_next_number(n)
        
        return True if n == 1 else False