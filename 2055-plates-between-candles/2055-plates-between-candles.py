class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prev_candle = [-1] * n
        next_candle = [n] * n
        prefix_sum_plates = [0] * n
        res = []
        
        # fill prev_candle
        for i in range(len(s)):
            if s[i] == '|':
                prev_candle[i] = i
            else:
                if i != 0:
                    prev_candle[i] = prev_candle[i-1]
        
        # fill next_candle
        for i in range(n-1,-1,-1):
            if s[i] == '|':
                next_candle[i] = i
            else:
                if i != n-1:
                    next_candle[i] = next_candle[i+1] 
        
        # fill prefix_sum_plates
        for i in range(len(s)):
            if s[i] == '*':
                if i != 0:
                    prefix_sum_plates[i] = prefix_sum_plates[i-1] + 1
                else:
                    prefix_sum_plates[i] = 1
            else:
                if i != 0:
                    prefix_sum_plates[i] = prefix_sum_plates[i-1]
                
                
        print(prefix_sum_plates)
        for query in queries:
            start, end = query[0], query[1]
            next_candle_idx = next_candle[start]
            prev_candle_idx = prev_candle[end]
            
            if next_candle_idx > end or prev_candle_idx < start:
                res.append(0)
            else:
                res.append(prefix_sum_plates[prev_candle_idx] - prefix_sum_plates[next_candle_idx])
        return res