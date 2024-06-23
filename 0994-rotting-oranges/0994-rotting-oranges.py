class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        queue = deque()
        remaining_oranges = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    remaining_oranges += 1
        
        minutes = 0
        while queue and remaining_oranges:
            directions = [[0,1], [1,0], [0,-1], [-1,0]]
            minutes += 1
            for i in range(len(queue)):
                x, y = queue.popleft()

                for dr, dc in directions:
                    dx = x + dr
                    dy = y + dc

                    if 0<=dx< row and 0<=dy<col and grid[dx][dy] == 1:
                        grid[dx][dy] = 2
                        queue.append((dx, dy))
                        remaining_oranges -= 1

        return minutes if remaining_oranges == 0 else -1
        