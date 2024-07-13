class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # Pair positions with their indices and sort based on positions
        sorted_pos = sorted((pos, i) for i, pos in enumerate(positions))
        stack = []
        
        for _, i in sorted_pos:
            if directions[i] == 'R':
                stack.append([i, healths[i]])
            else:
                while stack and directions[stack[-1][0]] == 'R':
                    if stack[-1][1] > healths[i]:
                        stack[-1][1] -= 1
                        break
                    elif stack[-1][1] < healths[i]:
                        healths[i] -= 1
                        stack.pop()
                    else:
                        stack.pop()
                        break
                else:
                    stack.append([i, healths[i]])
        
        # Sort the stack based on the original indices and return the healths
        stack.sort(key=lambda x: x[0])
        return [health for _, health in stack]
