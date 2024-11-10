class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j, res = 0, 0, []
        
        while i < len(firstList) and j < len(secondList):
            s1, e1 = firstList[i][0], firstList[i][1]
            s2, e2 = secondList[j][0], secondList[j][1]
            
            if s2 <= e1 and s1 <= e2:
                # The intersection is the max of start points and min of end points
                res.append([max(s1, s2), min(e1, e2)])
            
            # Move to the next interval in the list where the interval ends first
            if e1 < e2:
                i += 1
            else:
                j += 1
                
        return res
