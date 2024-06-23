class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i, j = 0, 0
        min_heap = []
        max_heap = []
        max_len = 0
        while j <= len(nums)-1:
            heapq.heappush(min_heap, (nums[j], j))
            heapq.heappush(max_heap, (-nums[j], j))
            while abs(min_heap[0][0] - (-max_heap[0][0])) > limit:
                i = min(min_heap[0][1], max_heap[0][1]) + 1
                
                while min_heap[0][1] < i:
                    heapq.heappop(min_heap)
                while max_heap[0][1] < i:
                    heapq.heappop(max_heap)
            
            max_len = max(max_len, j-i+1)
            j += 1
        return max_len
                
