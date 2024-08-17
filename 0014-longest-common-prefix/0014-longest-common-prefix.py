class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end_of_word = True
    
    def longest_common_prefix(self):
        curr = self.root
        prefix = []
        while curr and len(curr.children) == 1 and not curr.end_of_word:
            for ch in curr.children:
                prefix.append(ch)
            curr = curr.children[ch]
        return ''.join(prefix)
        

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            trie.add_word(word)
        return trie.longest_common_prefix()
        