class Solution:
    def euclidean_distance(self, x1,x2,y1,y2):
        return sqrt((x1-x2)**2 + (y1-y2)**2)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max heap 
        heap = []
        for point in points:
            x1, y1= point[0], point[1]
            x2, y2 = 0, 0
            edist = self.euclidean_distance(x1, x2, y1, y2)
            heapq.heappush(heap,(-edist, (x1,y1)))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = [ele[1] for ele in heap]
        
        return res