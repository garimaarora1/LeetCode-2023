class TrieNode:
    
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end_of_word = False
        self.ref = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def add_word(self, word):
        curr = self.root
        curr.ref += 1
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            curr.ref += 1
        curr.end_of_word = True
    
    def remove_word(self, word):
        curr = self.root
        curr.ref -= 1
        for ch in word:
            curr = curr.children[ch]
            curr.ref -= 1
        curr.end_of_word = False
    
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        def dfs(i, j, curr, word):
            
            if curr.end_of_word == True:
                res.append(word)
                trie_obj.remove_word(word)
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                
                if 0<=x<row and 0<=y<col and (x, y) not in visited and board[x][y] in curr.children and curr.children[board[x][y]].ref > 0:
                    visited.add((x, y))
                    dfs(x, y, curr.children[board[x][y]], word+board[x][y])
                    print(x, y)
                    visited.remove((x, y))
            
        trie_obj = Trie()
        curr = trie_obj.root
        
        for word in words:
            trie_obj.add_word(word)
        row = len(board)
        col = len(board[0])
        visited = set()
        res = []
        for i in range(row):
            for j in range(col):
                if board[i][j] in curr.children and curr.ref > 0:
                    visited.add((i, j))
                    dfs(i, j, curr.children[board[i][j]], board[i][j])
                    visited.remove((i, j))
        return res
                