class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[1, 0], [0, 1], [-1, 0], [0,-1]]
        
        def bfs(queue):
            visited = set()

            while queue:
                i, j = queue.popleft()
                visited.add((i, j))
                for dr, dc in directions:
                    dx = i + dr
                    dy = j + dc
                    if 0<=dx<row and 0<=dy<col and heights[dx][dy] >= heights[i][j] and (dx, dy) not in visited:
                        queue.append((dx, dy))
                        visited.add((dx, dy))
            return visited
                
            
        pacific_queue = deque()
        atlantic_queue = deque()
        
        row = len(heights)
        col = len(heights[0])
        
        for i in range(row):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, col-1))
        
        for i in range(col):
            pacific_queue.append((0, i))
            atlantic_queue.append((row-1, i))
            
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        
        return pacific_reachable.intersection(atlantic_reachable)