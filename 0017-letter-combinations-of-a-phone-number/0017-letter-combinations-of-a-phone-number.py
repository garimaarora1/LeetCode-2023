class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        key_map = {
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"
        }

        res = []
        
        def dfs(i, s):

            if i == len(digits):
                res.append(s)
                return
            
            for ch in key_map[digits[i]]:
                dfs(i+1, s+ch)
        
        dfs(0, '')
        return res