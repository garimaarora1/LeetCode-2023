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

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie_obj = Trie()
        trie_obj.add_word(strs[0])
        
        mini = float('inf')
        if len(strs) == 1:
            return strs[0]
        for word in strs[1:]:
            curr = trie_obj.root
            curr_count = 0
            for ch in word:
                if ch not in curr.children or mini <= curr_count:
                    break
                curr = curr.children[ch]
                curr_count += 1
            mini = min(mini, curr_count)
        return strs[0][:mini] if mini != float('inf') else ""
                
        
            
        