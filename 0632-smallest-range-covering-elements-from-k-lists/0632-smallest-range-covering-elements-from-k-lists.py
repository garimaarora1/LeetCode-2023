class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minx, miny = 0, float('inf')
        max_val = float('-inf')
        next_indices = [0] * len(nums)
        
        # Custom comparator for the priority queue to compare elements in the lists
        min_queue = [(nums[i][0], i) for i in range(len(nums))]
        heapq.heapify(min_queue)
        
        # Initialize the maximum value
        for i in range(len(nums)):
            max_val = max(max_val, nums[i][0])
        
        while True:
            min_val, min_idx = heapq.heappop(min_queue)
            
            # Update the range if it's smaller than the current best range
            if miny - minx > max_val - min_val:
                minx, miny = min_val, max_val
            
            # Move to the next element in the current list
            next_indices[min_idx] += 1
            if next_indices[min_idx] == len(nums[min_idx]):
                break
            
            # Add the next element of the current list to the priority queue
            heapq.heappush(min_queue, (nums[min_idx][next_indices[min_idx]], min_idx))
            max_val = max(max_val, nums[min_idx][next_indices[min_idx]])
        
        return [minx, miny]
