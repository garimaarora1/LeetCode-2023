class Solution:
    def reorganizeString(self, s: str) -> str:
        
        # adding all the values to hash map and store freq for each ch, key: ch, value: freq
        counter = defaultdict(int)
        for ch in s:
            counter[ch] += 1
        
        # add each key value pair to a max heap (freq, ch)
        heap = []
        for key, value in counter.items():
            heap.append((-value, key))
        heapq.heapify(heap)

        # res, prev
        res = ''
        prev = None
        
        # loop through the heap
        while heap or prev:
            if prev and not heap:
                return ""
            
            freq, ch = heapq.heappop(heap)
            freq += 1
            res += ch
            if prev:
                heapq.heappush(heap, prev)
                prev = None
            if freq!=0:
                prev = (freq, ch)
        
        # return result
        return res