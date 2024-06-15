class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        keep inserting in heap as long as I have the w that is needed for given project
        """
        capital_profits = [(capital[i], profits[i]) for i in range(len(profits))]
        capital_profits.sort()
        max_heap = []
        i = 0
        while i < len(profits):
            if w >= capital_profits[i][0]:
                heapq.heappush(max_heap, -capital_profits[i][1])
                i += 1
            elif k > 0 and max_heap:
                w += -heapq.heappop(max_heap)
                k -= 1
            else:
                break

        while k > 0 and max_heap:
            w += -heapq.heappop(max_heap)
            k -= 1
        return w
        
            
        
