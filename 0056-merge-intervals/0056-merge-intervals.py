class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        pair = intervals[0]
        res = []
        for start_time, end_time in intervals[1:]:
            if start_time <= pair[1]:
                pair[1] = max(pair[1], end_time)
            else:
                res.append(pair)
                pair = [start_time, end_time]
        
        res.append(pair)
        return res
        