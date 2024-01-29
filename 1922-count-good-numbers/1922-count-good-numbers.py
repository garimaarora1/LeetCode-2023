class Solution:
    MOD = (10 ** 9) + 7
    def recursive_pow(self, x, n) -> float:
        if n == 0:
            return 1
        if n % 2 != 0:    
            return (self.recursive_pow((x*x) % self.MOD, n//2) * x) % self.MOD
        else:
            return self.recursive_pow((x*x) % self.MOD, n//2) % self.MOD

    def countGoodNumbers(self, n: int) -> int:
        odd_pow = n // 2
        even_pow = (n // 2) + (n % 2)
        result = (self.recursive_pow(5, even_pow) * self.recursive_pow(4, odd_pow)) % self.MOD
        return result

