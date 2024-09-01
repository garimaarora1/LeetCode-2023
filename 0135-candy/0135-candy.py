class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = n
        i=1
        while i<n:
            if(ratings[i] == ratings[i-1]):
                i+=1
                continue
            
            peak=0
            while ratings[i]>ratings[i-1]:
                peak+=1
                candies+=peak
                i+=1
                if i==n:
                    return candies
            slope=0
            while i<n and ratings[i]<ratings[i-1]:
                slope+=1
                candies+=slope
                i+=1
            candies-=min(slope,peak)
            
        return candies
        