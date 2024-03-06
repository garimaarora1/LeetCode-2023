class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        if l == 1 and n == 1 and flowerbed[0] == 0:
            return 1
        for i in range(len(flowerbed)-1):
            if ((i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0) or 
                (i == l-2 and flowerbed[i] == 0 and flowerbed[i+1] == 0)):
                    flowerbed[i] = 1
                    n -= 1
            else:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0
                
                
        