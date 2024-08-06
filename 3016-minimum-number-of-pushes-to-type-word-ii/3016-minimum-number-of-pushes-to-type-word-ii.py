class Solution:
    def minimumPushes(self, word: str) -> int:
        freq_map = Counter(word)
        heap = [-freq for freq in freq_map.values()]
        heapq.heapify(heap)
        key, row = 0, 0
        min_count = 0
        while heap:
            row = (key // 8) + 1
            min_count += row * (-heapq.heappop(heap))
            key += 1
        return min_count
            
        
        