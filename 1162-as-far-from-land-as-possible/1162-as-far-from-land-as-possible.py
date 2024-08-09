class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        sources = deque([(r, c) for r in range(rows) for c in range(cols) if grid[r][c]])
        max_distance = -1

        if len(sources) == rows * cols:
            return max_distance

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while sources:
            for _ in range(len(sources)):
                cur_r, cur_c = sources.popleft()
                for dr, dc in directions:
                    new_r, new_c = cur_r + dr, cur_c + dc
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 0:
                        sources.append((new_r, new_c))
                        grid[new_r][new_c] = -1  # Mark as visited
            max_distance += 1

        return max_distance
