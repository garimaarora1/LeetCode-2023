class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        count = 0
        while num!=1:
            if num%2 == 0:
                num = num // 2
            else:
                num +=1 
            count += 1
        return count
        