class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.end_of_word = False
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
        curr.end_of_word = True
        curr.word = word
    
    def get_top_freq_words(self, remaining):
        
        def dfs(curr, res, remaining):
            
            if remaining[0] == 0:
                return

            if curr.word != None:
                remaining[0] -= 1
                res.append(curr.word)
                
            for i in range(26):
                ch = chr(ord('a') + i)
                if ch in curr.children:
                    dfs(curr.children[ch], res, remaining)
            return res
    
        curr = self.root
        return dfs(curr, [], remaining)


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        n = len(words)
        buckets = [Trie() for _ in range(n+1)]
        
        counter = Counter(words)
        
        for word, freq in counter.items():
            buckets[freq].insert(word)
            
        res = []
        remaining = [k]
        for i in range(n, 0, -1):
            if remaining[0] == 0:
                break
            
            words = buckets[i].get_top_freq_words(remaining)
            res.extend(words)
        return res
            
        