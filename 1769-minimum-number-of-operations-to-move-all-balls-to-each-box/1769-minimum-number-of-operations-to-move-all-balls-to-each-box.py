class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        # Prefix pass: left to right
        balls = 0  # Number of balls encountered so far
        ops = 0    # Number of operations to move all balls to the current position
        for i in range(n):
            answer[i] += ops
            if boxes[i] == '1':
                balls += 1
            ops += balls

        # Suffix pass: right to left
        balls = 0  # Reset number of balls for suffix pass
        ops = 0    # Reset number of operations for suffix pass
        for i in range(n-1, -1, -1):
            answer[i] += ops
            if boxes[i] == '1':
                balls += 1
            ops += balls

        return answer