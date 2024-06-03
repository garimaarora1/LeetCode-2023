class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        "11:43"
        
        """
        max - o(n)
        
        
        """
        maxCandies = max(candies)
        res = []
        for candy in candies:
            res.append(candy + extraCandies >= maxCandies)
        return res
        
        
        