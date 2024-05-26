class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # use hash map and heap
        # remember False cases: return False if it is not in hasp map and return False if it not on top of the heap
        if len(hand) % groupSize != 0:
            return False
        
        counter = Counter(hand)
        heap = [key for key in counter.keys()]
        heapq.heapify(heap)
        
        while heap:
            mini = heap[0]
            for i in range(mini, mini+groupSize):
                if i not in counter:
                    return False
                counter[i] -= 1
                if counter[i] == 0:
                    if i!=heap[0]:
                        return False
                    heapq.heappop(heap)
        return True
        
        