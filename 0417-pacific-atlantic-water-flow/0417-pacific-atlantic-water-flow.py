class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:

        def bfs(queue):
            visited = set()
            while queue:
                x, y = queue.popleft()
                visited.add((x, y))
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dr, dc in directions: 
                    dx, dy = x + dr, y + dc
                    if 0 <= dx < rows and 0 <= dy < cols and (dx, dy) not in visited and matrix[dx][dy] >= matrix[x][y]:
                        queue.append((dx, dy))
            return visited
    
    
        rows, cols = len(matrix), len(matrix[0])
        
        
        pacific_queue = deque()
        atlantic_queue = deque()
        for i in range(rows):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, cols - 1))
        for i in range(cols):
            pacific_queue.append((0, i))
            atlantic_queue.append((rows - 1, i))
            
            
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)

        return list(pacific_reachable.intersection(atlantic_reachable))