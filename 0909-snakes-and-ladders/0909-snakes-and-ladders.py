class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        visited = set()
        q = deque()
        # Start from the first cell
        q.append((1, 0))
        visited.add(1)
        n = len(board)
        
        def position(sq):
            r = (sq - 1) // n
            c = (sq - 1) % n
            if r % 2:
                c = (n - 1 - c)
            return (r, c)

        while q:
            curMove, moves = q.popleft()
            if curMove == n * n:
                return moves
            
            for i in range(1, 7):
                nextMove = curMove + i
                if nextMove > n * n:
                    break
                
                r, c = position(nextMove)
                if r < n and c < n and board[r][c] != -1:
                    nextMove = board[r][c]
                
                if nextMove not in visited:
                    visited.add(nextMove)
                    q.append((nextMove, moves + 1))
        
        return -1