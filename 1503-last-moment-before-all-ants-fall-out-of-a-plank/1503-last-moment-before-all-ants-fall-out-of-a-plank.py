class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        l, r = 0, 0
        if left:
            l = max(left)
        if right:
            r = min(right)
            r = n - r
        return(max(l,r))
        