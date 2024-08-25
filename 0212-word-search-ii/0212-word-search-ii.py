class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        self.ref = 0

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        curr.ref += 1
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            curr.ref += 1
        curr.end_of_word = True
    
    def remove(self, word):
        curr = self.root
        curr.ref -= 1
        for ch in word:
            curr = curr.children[ch]
            curr.ref -= 1
        curr.end_of_word = False
            
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        words_found = []
        
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        def dfs(i, j, curr, prefix):
            
            if curr.end_of_word:
                trie.remove(prefix)
                words_found.append(prefix)
            
            for dr, dc in directions:
                dx = i + dr
                dy = j + dc
                
                if 0<=dx<row and 0<=dy<col and board[dx][dy] in curr.children and (dx, dy) not in visited and curr.ref > 0:
                    visited.add((dx, dy))
                    dfs(dx, dy, curr.children[board[dx][dy]], prefix+board[dx][dy])
                    visited.remove((dx, dy))
                
            
        trie = Trie()
        curr = trie.root
        
        for word in words:
            trie.insert(word)

        row = len(board)
        col = len(board[0])
        visited = set()
        
        for i in range(row):
            for j in range(col):
                if board[i][j] in curr.children and curr.ref > 0:
                    visited.add((i, j))
                    dfs(i, j, curr.children[board[i][j]], board[i][j])
                    visited.remove((i, j))
        return words_found
        