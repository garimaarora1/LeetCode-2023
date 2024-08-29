class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        # max heap
        heap = [-value for value in counter.values()]
        heapq.heapify(heap)
        row = 1
        key = 0
        total_key_pushes = 0
        while heap:
            freq = -heapq.heappop(heap)
            row = key // 8 + 1
            total_key_pushes += (freq * row)
            key += 1
        return total_key_pushes
        