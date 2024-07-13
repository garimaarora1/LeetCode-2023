class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        sorted_pos = [(pos, i) for i, pos in enumerate(positions)]
        sorted_pos.sort()
        stack = []
        for pos, i in sorted_pos:
            if directions[i] == 'R':
                stack.append([i, healths[i]])
            else:
                while stack and  directions[stack[-1][0]] == 'R' and stack[-1][1] < healths[i]:
                    stack.pop()
                    healths[i] -= 1
                if stack and directions[stack[-1][0]] == 'R' and stack[-1][1] > healths[i]:
                    stack[-1][1] -= 1
                    continue
                if not stack or (directions[stack[-1][0]] == 'L'):
                    stack.append([i, healths[i]])
                if directions[stack[-1][0]] == 'R' and stack[-1][1] == healths[i]:
                    stack.pop()
        
        stack.sort()
        return [health for i, health in stack]