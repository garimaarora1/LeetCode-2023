class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        ans = 1
        end = points[0][1]
        for i in points:
            if i[0]>end:
                ans+=1
                end = i[1]
        return ans
