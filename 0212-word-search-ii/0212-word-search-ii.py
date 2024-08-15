class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.reference = 0
        self.end_of_word = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr.children[ch].reference += 1
            curr = curr.children[ch]
            
        curr.end_of_word = True
        
    def remove_word(self, word):
        curr = self.root
        for ch in word:
            curr.children[ch].reference -= 1
            curr = curr.children[ch]
        curr.end_of_word = False

        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        
        def dfs(i, j, curr_node, curr_word):
            if curr_node.end_of_word == True:
                res.append(curr_word)
                trie_obj.remove_word(curr_word)
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                
                if 0<=x<row and 0<=y<col and (x,y) not in visited and board[x][y] in curr_node.children and curr_node.children[board[x][y]].reference > 0:
                    visited.add((x, y))
                    dfs(x, y, curr_node.children[board[x][y]], curr_word + board[x][y])
                    visited.remove((x, y))
                    
        
        
        row = len(board)
        col = len(board[0])
        visited = set()
        res = []
        trie_obj = Trie()
        curr_node = trie_obj.root
        
        for word in words:
            trie_obj.add_word(word)

        for i in range(row):
            for j in range(col):
                if board[i][j] in curr_node.children:
                    visited.add((i, j))
                    dfs(i, j, curr_node.children[board[i][j]], board[i][j])
                    visited.remove((i, j))
        return res