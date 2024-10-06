class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n = len(word)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        def dfs(i, j, curr_idx):
            if curr_idx == n:
                return True
            
            for dr, dc in directions:
                dx = i + dr
                dy = j + dc
                
                if 0<=dx<row and 0<=dy<col and board[dx][dy] == word[curr_idx] and (dx, dy) not in visited:
                    visited.add((dx, dy))
                    if dfs(dx, dy, curr_idx+1):
                        return True
                    visited.remove((dx, dy))
            return False

            
        row = len(board)
        col = len(board[0])
        
        visited = set()
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and (i, j) not in visited:
                    visited.add((i, j))
                    if dfs(i, j, 1):
                        return True
                    visited.remove((i, j))
        return False
        
        