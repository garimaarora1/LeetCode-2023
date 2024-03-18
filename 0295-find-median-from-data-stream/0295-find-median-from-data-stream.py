# good explanation: https://leetcode.com/problems/find-median-from-data-stream/discuss/2492199/Python-3-Min-heap-and-Max-heap-approach-explained
class MedianFinder:

    def __init__(self):
        self.first_half = []
        self.second_half = []

    def addNum(self, num: int) -> None:
        heappush(self.first_half, -num)
        popped_element = heappop(self.first_half)
        heappush(self.second_half, -popped_element)
        
        if len(self.first_half) < len(self.second_half):
            popped_element = heappop(self.second_half)
            heappush(self.first_half, -popped_element)
        

    def findMedian(self) -> float:
        if len(self.first_half) == len(self.second_half):
            return (-self.first_half[0] + self.second_half[0]) / 2
        return -self.first_half[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()