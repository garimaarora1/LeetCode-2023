class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        prev = None
        
        # max_heap
        heap = []
        for key, value in counter.items():
            heap.append((-value, key))
        heapq.heapify(heap)
        res = ""

        while prev or heap:
            if prev and not heap:
                return ""
            
            freq, ch = heapq.heappop(heap)
            freq += 1
            res += ch

            if prev:
                heapq.heappush(heap, prev)
                prev = None
            if freq != 0:
                prev = (freq, ch)
        return res
                
            