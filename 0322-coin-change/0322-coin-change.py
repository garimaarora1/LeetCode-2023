class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        visited = set()
        queue = deque()
        queue.append((amount, 0))
        while queue:
            curr_amount, steps = queue.popleft()
            if curr_amount == 0:
                return steps
            for coin in coins:
                if curr_amount-coin >= 0 and curr_amount-coin not in visited :
                    queue.append((curr_amount-coin, steps+1))
                    visited.add(curr_amount-coin)
        return -1
            
        
        

        