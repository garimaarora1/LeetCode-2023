class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        roll_sum = 0
        for roll in rolls:
            roll_sum += roll
        total_sum = mean * (n+len(rolls))
        n_sum = total_sum - roll_sum
        if n_sum/n < 1 or n_sum/n >6:
            return []
        result = []
        while n_sum > 0:
            possibility = n_sum//n
            result.append(possibility)
            n_sum -= possibility
            n -= 1
        return result
        
        
        
        