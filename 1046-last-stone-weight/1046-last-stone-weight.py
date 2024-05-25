class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heap = stones
        heapq.heapify(heap)
        
        while len(heap) > 1:
            num1 = -heapq.heappop(heap)
            num2= -heapq.heappop(heap)
            if num1 != num2:
                heapq.heappush(heap, -(num1-num2))
        return -heap[0] if heap else 0