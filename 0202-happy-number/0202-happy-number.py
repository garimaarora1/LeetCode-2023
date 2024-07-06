class Solution:
    def get_next_number(self, n, total_sum):
        
        if n == 0:
            return total_sum
        last_digit = n % 10
        n = n // 10
        total_sum += last_digit**2
            
        return self.get_next_number(n, total_sum)

        
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            n = self.get_next_number(n, 0)
        
        return True if n == 1 else False