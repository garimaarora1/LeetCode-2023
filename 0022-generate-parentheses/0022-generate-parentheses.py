class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def dfs(s, o, c):
            if o == 0 and c == 0:
                res.append(''.join(s))
                return
            if o>0:
                s.append("(")
                dfs(s, o-1, c)
                s.pop()
            if o<c:
                s.append(")")
                dfs(s, o, c-1)
                s.pop()
            
        
        dfs([], n, n)
        return res