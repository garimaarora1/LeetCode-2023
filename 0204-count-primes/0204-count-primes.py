class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        numbers = [True] * (n)
        numbers[0] = numbers[1] = False

        for p in range(2, int(sqrt(n)) + 1):
            if numbers[p]:
                # Set all multiples of p to false because they are not prime.
                for multiple in range(p * p, n, p):
                    numbers[multiple] = False

        return sum(numbers)