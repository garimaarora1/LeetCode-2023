class Solution:
    def recursive_pow(self, x, n) -> float:
        if n == 0:
            return 1
        if n % 2 != 0:    
            return (self.recursive_pow((x*x) % (10**9 + 7), n//2) * x) % (10**9 + 7)
        else:
            return self.recursive_pow((x*x) % (10**9 + 7), n//2) % (10**9 + 7)

    def countGoodNumbers(self, n: int) -> int:
        if n%2 == 0:
            o_pow = e_pow = n//2
        else:
            o_pow, e_pow = n//2, n//2+1
        result = (self.recursive_pow(5, e_pow) * self.recursive_pow(4, o_pow)) % (10**9 + 7)
        return(result)


