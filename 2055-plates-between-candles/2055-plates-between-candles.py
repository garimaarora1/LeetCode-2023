class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prev_candles = [-1] * n
        next_candles = [n] * n
        prefix_sum = [0] * n
        ans = []
        for i in range(n):
            if s[i] == '|':
                prev_candles[i] = i
            else:       
                if i!=0:
                    prev_candles[i] = prev_candles[i-1]
        for i in range(n-1, -1, -1):
            if s[i] == '|':
                next_candles[i] = i
            else:
                if i != n-1:
                    next_candles[i] = next_candles[i+1]
        for i in range(n):
            if s[i] == '*':
                if i == 0:
                    prefix_sum[i] = 1
                else:
                    prefix_sum[i] = prefix_sum[i-1] + 1
            else:
                if i != 0:
                    prefix_sum[i] = prefix_sum[i-1]
        for query in queries:
            start = next_candles[query[0]]
            end = prev_candles[query[1]]
            if start > query[1] or end < query[0]:
                ans.append(0)
                continue
            ans.append(prefix_sum[end] - prefix_sum[start])
        return ans
            
            
            
        
                