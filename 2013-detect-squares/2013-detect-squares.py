class DetectSquares:
    def __init__(self):
        self.counter = Counter()

    def add(self, point: List[int]) -> None:
        self.counter[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        x1, y1 = point
        for x2, y2 in self.counter:
            if abs(x1-x2)==abs(y1-y2) and (x1!=x2 or y1!=y2):
                ans += self.counter[(x2, y2)] * self.counter[(x1, y2)] * self.counter[(x2, y1)]
        return ans