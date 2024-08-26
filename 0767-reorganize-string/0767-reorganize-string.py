class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        max heap, counter, prev, res
        """
        counter = Counter(s)
        max_heap = []
        for key, value in counter.items():
            max_heap.append((-value, key))
        heapq.heapify(max_heap)
        
        prev = None
        res = ''
        
        while max_heap or prev:
            if prev and not max_heap:
                return ''
            
            freq, ch = heapq.heappop(max_heap)
            
            res += ch
            freq += 1
            
            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            
            if freq != 0:
                prev = (freq, ch)
        return res