class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        res = []
        for candy in candies:
            res.append(candy + extraCandies >= maxCandies)
        return res
        
        
        