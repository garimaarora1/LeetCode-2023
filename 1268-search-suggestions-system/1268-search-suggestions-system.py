from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.word = None
        self.child = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str):
        curr = self.root
        for c in word:
            curr = curr.child[c]
        curr.word = word

    def getWords(self, node: TrieNode, limit: int) -> List[str]:
        words = []

        def dfs(curr: TrieNode):
            if len(words) == limit:
                return
            if curr.word is not None:
                words.append(curr.word)
            for c in sorted(curr.child.keys()):
                dfs(curr.child[c])

        dfs(node)
        return words

    def searchPrefix(self, prefix: str) -> List[List[str]]:
        curr = self.root
        result = []
        for c in prefix:
            if curr is not None and c in curr.child:
                curr = curr.child[c]
                result.append(self.getWords(curr, 3))
            else:
                curr = None
                result.append([])
        return result

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.addWord(product)
        
        return trie.searchPrefix(searchWord)
