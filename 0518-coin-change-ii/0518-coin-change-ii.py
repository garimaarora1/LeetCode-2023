class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1] * (amount+1) for i in range(len(coins))]

        def helper(i, curr_amount):
            if i == len(coins):
                if curr_amount == 0:
                    return 1
                return 0

            if dp[i][curr_amount] != -1:
                return dp[i][curr_amount]
            
            not_pick = helper(i+1, curr_amount)
            pick = 0
            if coins[i] <= curr_amount:
                pick = helper(i, curr_amount - coins[i])
            
            dp[i][curr_amount] = pick + not_pick
            return dp[i][curr_amount]
        
        return helper(0, amount)
