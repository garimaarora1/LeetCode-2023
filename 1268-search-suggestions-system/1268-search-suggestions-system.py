class TrieNode:
    
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.word = word
    
    def get_words(self, curr, limit):
        res = []
        def dfs(curr):
            if len(res) == limit:
                return
            if curr.word != None:
                res.append(curr.word)
            for i in range(26):
                ch = chr(ord('a') + i)
                if ch in curr.children:
                    dfs(curr.children[ch])

        dfs(curr)
        return res
            
    def get_suggestions(self, word):
        curr = self.root
        suggestions = []

        for ch in word:
            if curr != None and ch in curr.children:
                curr = curr.children[ch]
                suggestions.append(self.get_words(curr, 3))
            
            else:
                curr = None
                suggestions.append([])
        return suggestions

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        trie = Trie()
        for product in products:
            trie.insert(product)
        
        return trie.get_suggestions(searchWord)