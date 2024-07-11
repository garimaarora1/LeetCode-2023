class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []  # for keeping track of indices of opening braces 
        res = [] # for storing the resultant string
        
        for ch in s:
            if ch == '(':
                stack.append(len(res))
            elif ch == ')':
                start = stack.pop()
                res[start:] = res[start:][::-1]
            else:
                res.append(ch)
        
        return ''.join(res)