class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        do two passes
        in first pass remove the pair with higher score
        in second pass remove the pair with lower score
        """
        def remove_pair(pair, points):
            nonlocal s
            stack = []
            curr_points = 0
            for ch in s:
                if stack and stack[-1] == pair[0] and ch == pair[1]:
                    stack.pop()
                    curr_points += points
                else:
                    stack.append(ch)
            s = ''.join(stack)
            return curr_points


        max_points = 0
        pair = "ab" if x > y else "ba"
        max_points += remove_pair(pair, max(x, y))
        max_points += remove_pair(pair[::-1], min(x, y))
        return max_points
        
        