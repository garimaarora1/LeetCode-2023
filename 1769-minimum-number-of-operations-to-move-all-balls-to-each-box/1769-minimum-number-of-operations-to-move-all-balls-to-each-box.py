class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0]*n
        for i in range(n):
            if boxes[i] == '1':
                for j in range(n):
                    res[j] += abs(i-j)
        return res