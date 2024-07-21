class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
    
        cost = defaultdict(list)
        n = len(points)
        
        for i in range(n):
            for j in range(i+1, n):
                x1, y1, x2, y2 = points[i][0], points[i][1], points[j][0], points[j][1]
                manhattan_distance = abs(x1-x2) + abs(y1-y2)
                cost[i].append((manhattan_distance, j))
                cost[j].append((manhattan_distance, i))

        visited = set()
        visited.add(0)
        heap = cost[0]
        ans = 0
        heapq.heapify(heap)
        count = 1
        # rmwa
        while heap:  
            dist, point = heapq.heappop(heap)
            if point not in visited:
                count += 1
                visited.add(point)
                for adj in cost[point]:
                    heapq.heappush(heap, adj)
                ans += dist
            if count >= n: 
                break
        return ans
            