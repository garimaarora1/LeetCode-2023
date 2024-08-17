class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        n = len(word)
        def dfs(i, j, curr_idx):
            if curr_idx == n:
                return True
    
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                
                if 0<=x< row and 0<=y<col and (x, y) not in visited and board[x][y] == word[curr_idx]:
                    visited.add((x, y))
                    if dfs(x, y, curr_idx+1):
                        return True
                    visited.remove((x, y))
            
            return False

        row = len(board)
        col = len(board[0])
        visited = set()
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if dfs(i, j, 1):
                        return True
                    visited.remove((i, j))
        return False