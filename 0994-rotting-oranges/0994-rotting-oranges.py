class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        calculate fresh oranges, rotten oranges, rotten organges go in queue, return minutes if fresh oranges == 0 else -1
        also only do bps uptil you have fresh organges and queu
        """
        row = len(grid)
        col = len(grid[0])
        queue = deque()
        remaining_oranges = 0
        minutes = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    remaining_oranges += 1
        
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while queue and remaining_oranges:
            n = len(queue)
            for _ in range(n):
                i, j = queue.popleft()
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    
                    if 0<=x<row and 0<=y<col and grid[x][y] == 1:
                        grid[x][y] = 2
                        queue.append((x, y))
                        remaining_oranges -= 1
            minutes += 1
        return minutes if remaining_oranges == 0 else -1
        