class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {'}': '{', ']': '[', ')': '('}
        stack = []
        for bracket in s:
            if bracket in parentheses_map.keys() and stack and stack[-1] == parentheses_map[bracket]:
                stack.pop()
            else:
                stack.append(bracket)
        return stack == []