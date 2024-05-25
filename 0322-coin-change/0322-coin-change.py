class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        visited_set = set()
        queue = deque()
        queue.append((0,0))
        while queue:
            coin, steps = queue.popleft()
            if coin == amount:
                return steps
            for i in coins:
                if coin + i <= amount and coin+i not in visited_set:
                    queue.append((coin+i,steps+1))
                    visited_set.add(coin+i)
        return -1
        