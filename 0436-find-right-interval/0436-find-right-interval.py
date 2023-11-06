class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        mapping = {}
        for idx, interval in enumerate(intervals):
            mapping[interval[0]] = idx
        print("mapping:", mapping)
        intervals.sort()
        n = len(intervals)

        def binary_search(intervals, target):
            left = 0
            right = n-1
            while left <= right:
                mid = left + (right-left)//2
                if intervals[mid][0] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            if left == n:
                return -1
            else:
                return left

        res = [-1] * n
        for i in range(n):
            idx2 = binary_search(intervals, intervals[i][1])
            if idx2 != -1:
                res[mapping[intervals[i][0]]] = mapping[intervals[idx2][0]]
            else:
                res[mapping[intervals[i][0]]] = -1
        
        return res