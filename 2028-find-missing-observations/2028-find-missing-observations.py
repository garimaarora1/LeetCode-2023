class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        given_sum = 0
        res = []
        for roll in rolls:
            given_sum += roll
        total_sum = mean * (len(rolls) + n)
        n_sum = total_sum - given_sum
        ele_sum = n_sum/n
        
        if not 1<=ele_sum<=6:
            return []
        
        while n_sum:
            ele = n_sum // n
            n_sum -= ele
            res.append(ele)
            n -= 1
        return res
            
        
        
        