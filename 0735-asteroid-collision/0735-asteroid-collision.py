class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        [10, 4, -5]
        for asteroid in asteroids:
            if asteroid < 0:
                while stack and stack[-1] > 0:
                    if stack[-1] >= abs(asteroid):
                        break
                    else:
                        stack.pop()
                if stack and stack[-1] > 0 and stack[-1] == abs(asteroid):
                    stack.pop()
                    continue
                if not stack or (stack and stack[-1] < 0):
                    stack.append(asteroid)
            else:
                stack.append(asteroid)
        return stack   
                