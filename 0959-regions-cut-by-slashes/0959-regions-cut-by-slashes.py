class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        dots = len(grid) + 1
        parent = [i for i in range(dots*dots)]
        count = 1
        
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            if parent_x != parent_y:
                if parent_x < parent_y:
                    parent[parent_y] = parent_x
                else:
                    parent[parent_x] = parent_y
                return False
            return True
        
        for i in range(dots):
            for j in range(dots):
                if i == 0 or j == 0 or i == dots-1 or j == dots-1:
                    pos = i * dots + j
                    union(0, pos)
    
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == ' ':
                    continue
                if grid[i][j] == '/':
                    # point1 = (i+1, j)
                    # point2 = (i, j+1)
                    pos1 = (i+1) * dots + j
                    pos2 = i * dots + j + 1
                    if union(pos1, pos2):
                        count += 1
                elif grid[i][j] == "\\":
                    # point1 = (i,j)
                    # point2 = (i+1, j+1)
                    pos1 = i * dots + j
                    pos2 = (i+1) * dots + j + 1
                    if union(pos1, pos2):
                        count += 1
        return count