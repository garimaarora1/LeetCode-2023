class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        "11:43"
        
        """
        max - o(n)
        
        
        """
        maxi = max(candies)
        res = []
        for candy in candies:
            if candy + extraCandies >= maxi:
                res.append(True)
            else:
                res.append(False)
        return res
        
        
        