class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {'}': '{', ']': '[', ')': '('}
        stack = []
        
        for parentheses in s:
            if parentheses in parentheses_map:
                if not stack or stack[-1] != parentheses_map[parentheses]:
                    return False
                stack.pop()
            else:
                stack.append(parentheses)
        return stack == []