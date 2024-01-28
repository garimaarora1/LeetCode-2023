class Solution:
    def recursive_pow(self, x, n) -> float:
        if n == 0:
            return 1
        if n % 2 != 0:    
            return self.recursive_pow(x*x, n//2) * x
        else:
            return self.recursive_pow(x*x, n//2)

    def myPow(self, x: float, n: int) -> float: 
        if n >= 0:
            return self.recursive_pow(x, abs(n))
        else:
            return self.recursive_pow(1/x, abs(n))
            
   