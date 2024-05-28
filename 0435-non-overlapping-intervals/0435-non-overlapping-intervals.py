class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        curr_end_time = float('-inf')
        overlapping_intervals = 0
        for start_time, end_time in intervals:
            if start_time >= curr_end_time:
                curr_end_time = end_time
            else:
                overlapping_intervals += 1
        return overlapping_intervals
                
                