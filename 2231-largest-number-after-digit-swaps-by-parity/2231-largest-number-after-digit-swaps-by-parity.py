class Solution:
    def largestInteger(self, num: int) -> int:
        digits = list(map(int, str(num)))

        # max heaps
        odd_heap = []
        even_heap = []

        for d in digits:
            if d % 2 == 0:
                heapq.heappush(even_heap, -d)
            else:
                heapq.heappush(odd_heap, -d)

        result = []
        for d in digits:
            if d % 2 == 0:
                result.append(-heapq.heappop(even_heap))  # Pop the largest even digit
            else:
                result.append(-heapq.heappop(odd_heap))  # Pop the largest odd digit

        return int("".join(map(str, result)))