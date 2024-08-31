class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Create a max-heap (using negative units per box for max-heap behavior)
        max_heap = [(-units, boxes) for boxes, units in boxTypes]
        heapq.heapify(max_heap)
        
        unit_count = 0
        
        # Process the heap until the truck is full or the heap is empty
        while max_heap and truckSize > 0:
            units, boxes = heapq.heappop(max_heap)
            boxes_to_take = min(truckSize, boxes)
            unit_count += boxes_to_take * -units  # Negate units to get the actual value
            truckSize -= boxes_to_take
        
        return unit_count
