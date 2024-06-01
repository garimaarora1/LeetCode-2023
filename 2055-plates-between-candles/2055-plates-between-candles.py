class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prev_candles = [0] * n
        next_candles = [0] * n
        prefix_sum = [0] * n
        ans = []
        for i in range(len(s)):
            if s[i] == '*':
                if i != 0:
                    prev_candles[i] = prev_candles[i-1] 
            else:
                prev_candles[i] = i

            if s[n-i-1] == "*":
                if i != 0:
                    next_candles[n-i-1] = next_candles[n-i]
            else:
                next_candles[n-i-1] = n-i-1

            if i != 0:
                prefix_sum[i] += prefix_sum[i-1]
            if s[i] == "*":
                prefix_sum[i] += 1

        for query in queries:
            start = next_candles[query[0]]
            end = prev_candles[query[1]]
            if start > query[1] or end < query[0]:
                ans.append(0)
                continue
            ans.append(prefix_sum[end] - prefix_sum[start])
        return ans
            
            
            
        
                