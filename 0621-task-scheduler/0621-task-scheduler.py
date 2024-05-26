class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        # max heap
        heap = [-cnt for cnt in counter.values()]
        heapq.heapify(heap)
        queue = deque()
        time = 0
        while heap or queue:
            time += 1
            if heap:
                val = 1 + heapq.heappop(heap)
                if val !=0:
                    queue.append((val, time+n))

            if queue:
                if queue[0][1] == time:
                    heapq.heappush(heap, queue.popleft()[0])
        return time
        