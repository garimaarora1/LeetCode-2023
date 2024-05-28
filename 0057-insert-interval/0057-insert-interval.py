class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        low, high = 0, len(intervals)-1
        target = newInterval[0]
        # binary search 
        while low <= high:
            mid = low + (high-low) // 2
            if intervals[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        # insert
        intervals.insert(low, newInterval)
        
        # merge intervals
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res