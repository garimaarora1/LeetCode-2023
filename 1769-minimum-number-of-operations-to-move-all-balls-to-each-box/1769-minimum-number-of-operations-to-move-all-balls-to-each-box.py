class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        balls = 0  
        ops = 0    
        for i in range(n):
            answer[i] += ops
            if boxes[i] == '1':
                balls += 1
            ops += balls

        balls = 0  
        ops = 0    
        for i in range(n-1, -1, -1):
            answer[i] += ops
            if boxes[i] == '1':
                balls += 1
            ops += balls

        return answer