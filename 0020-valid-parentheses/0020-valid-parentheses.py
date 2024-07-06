class Solution:
    def isValid(self, s: str) -> bool:
        braces_map = {']': '[', '}': '{', ')': '('}
        stack = []
        for bracket in s:
            if bracket in braces_map:
                if not stack or stack[-1] != braces_map[bracket]:
                    return False
                stack.pop()
            else:
                stack.append(bracket)
        return stack == []
        