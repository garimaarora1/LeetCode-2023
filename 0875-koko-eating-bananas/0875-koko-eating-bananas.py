class Solution:
    def can_finish(self, h, piles, k):
        hours = 0
        for pile in piles:
            hours += ceil(pile/k)
            if hours > h:
                return False
        return hours <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if self.can_finish(h, piles, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans