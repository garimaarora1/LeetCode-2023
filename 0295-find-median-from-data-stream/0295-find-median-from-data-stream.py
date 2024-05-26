# maintain two heaps
# first: max heap
# second: min heap 
# algo: add element to first heap, get the max value and add to second heap, if len first < second: get the min value from second heap and add to first heap 
class MedianFinder:

    def __init__(self):
        self.first_heap = []
        self.second_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.first_heap, -num)
        max_num = -heapq.heappop(self.first_heap)
        heapq.heappush(self.second_heap, max_num)
        
        if len(self.first_heap) < len(self.second_heap):
            min_num = -heapq.heappop(self.second_heap)
            heapq.heappush(self.first_heap, min_num)
        

    def findMedian(self) -> float:
        if len(self.first_heap) == len(self.second_heap):
            return (-self.first_heap[0] +self.second_heap[0]) / 2
        return -self.first_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()