class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        # max_heap
        heap = []
        
        for key, value in counter.items():
            heapq.heappush(heap, (-value, key))
        heapq.heapify(heap)
        
        prev = None
        res = ''
        
        while heap or prev:
            if prev and not heap:
                return ""
            
            freq, ch = heapq.heappop(heap)
            res += ch
            freq += 1
            
            if prev:
                heapq.heappush(heap, prev)
                prev = None
            if not prev:
                if freq != 0:
                    prev = (freq, ch)
        
        return res