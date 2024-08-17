class TrieNode:
    def __init__(self):
        self.word = None
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str):
        curr = self.root
        for ch in word:
            curr = curr.children[ch]
        curr.word = word

    def getWords(self, node, limit):
        words = []

        def dfs(curr):
            if len(words) == limit:
                return
            if curr.word is not None:
                words.append(curr.word)
                
            for i in range(26):
                ch = chr(ord('a') + i)
                if ch in curr.children:
                    dfs(curr.children[ch])

        dfs(node)
        return words

    def searchPrefix(self, prefix):
        curr = self.root
        result = []
        for ch in prefix:
            if curr is not None and ch in curr.children:
                curr = curr.children[ch]
                result.append(self.getWords(curr, 3))
            else:
                curr = None
                result.append([])
        return result

class Solution:
    def suggestedProducts(self, products, searchWord):
        trie = Trie()
        for product in products:
            trie.addWord(product)
        
        return trie.searchPrefix(searchWord)
