class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {'}': '{', ']': '[', ')': '('}
        stack = []
        for bracket in s:
            if bracket in parentheses_map:
                if not stack or stack[-1] != parentheses_map[bracket]:
                    return False
                stack.pop()
            else:
                stack.append(bracket)
        return stack == []