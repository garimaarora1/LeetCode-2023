class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
        # Case 1: intervals fixed before new interval
        while i<n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # Case 2: overapping intervals
        # important
        while i<n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        # important
        res.append(newInterval)
    
        
        # Case 3: intervals to happesn post new internval
        while i<n and intervals[i][0] > newInterval[1]:
            res.append(intervals[i])
            i += 1
        return res