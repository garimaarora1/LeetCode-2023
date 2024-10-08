class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        queue = deque()
        visited = set()
        ones = 0
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    visited.add((i, j))
                    queue.append((i, j))
                else:
                    ones += 1
                    
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        curr_dist = 1

        while queue and ones:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    if 0<=x<row and 0<=y<col and (x, y) not in visited:
                        ones -= 1
                        mat[x][y] = curr_dist
                        visited.add((x, y))
                        queue.append((x, y))
            
            curr_dist += 1
        
        return mat
            
                    
        