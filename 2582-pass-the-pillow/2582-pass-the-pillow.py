class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = time // (n-1)
        additional_people = time % (n-1)
        
        if direction % 2 == 0:
            return 1 + additional_people
        return n - additional_people