class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_map = {')': '(', ']': '[', '}': '{'}
        for parentheses in s:
            if parentheses in parentheses_map:
                if not stack or stack[-1] != parentheses_map[parentheses]:
                    return False
                stack.pop()
            else:
                stack.append(parentheses)
        
        return stack == []
        