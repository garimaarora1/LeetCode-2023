class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        pair = intervals[0]
        res = []
        for interval in intervals[1:]:
            if pair[1] >= interval[0]:
                pair[1] = max(pair[1], interval[1])
            else:
                res.append(pair)
                pair = interval
        res.append(pair)
        return res