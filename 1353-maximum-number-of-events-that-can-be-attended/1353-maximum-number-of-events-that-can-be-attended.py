class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # 1. sort the events based on start time
        # 2. check what events can be attended today and add those evenet's end time to heap
        # 3. remove evetns whose end time has gone from the heap
        # 4. attend the event that can be attended today
        # really good explanation: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/discuss/1116371/Python-With-detailed-explanation
        
        events.sort()
        max_days = max(end for start, end in events)
        curr_day = min(start for start, end in events)
        i = 0
        n = len(events)
        heap = []
        count = 0
        
        while curr_day <= max_days:
            while i < n and events[i][0] == curr_day:
                heapq.heappush(heap, events[i][1])
                i += 1
            while heap and heap[0] < curr_day:
                heapq.heappop(heap)
            
            if heap:
                heapq.heappop(heap)
                count += 1
            curr_day += 1
        return count
        
        