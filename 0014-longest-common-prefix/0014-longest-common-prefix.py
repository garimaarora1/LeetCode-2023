class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end_of_word = True
    
    def get_longest_common_prefix(self):
        curr = self.root
        res = ''
        while len(curr.children) == 1 and not curr.end_of_word:
            for ch in curr.children:
                res += ch
            curr = curr.children[ch]
        return res
                
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            trie.insert(word)
        return trie.get_longest_common_prefix()