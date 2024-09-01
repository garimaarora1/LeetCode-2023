class Solution:
    def intToRoman(self, num: int) -> str:
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        res = ''
        for i in range(len(vals)):
            while num >= vals[i]:
                res += symbols[i]
                num -= vals[i]
        return res        
