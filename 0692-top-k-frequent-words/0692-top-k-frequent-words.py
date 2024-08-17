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
    
    def get_word(self, curr, prefix, remaining):
        res = []
        if remaining[0] == 0:
            return res
        
        if curr.end_of_word == True:
            remaining[0] -= 1
            res.append(prefix)
            
        for i in range(26):
            ch = chr(ord('a') + i)
            if ch in curr.children:
                curr_res = self.get_word(curr.children[ch], prefix + ch, remaining)
                res += curr_res
        return res
        

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        n = len(words)
        counter = Counter(words)
        
        buckets = [Trie() for _ in range(n+1)]
        
        for word, freq in counter.items():
            buckets[freq].add_word(word)
        
        remaining = [k]
        res = []
        for i in range(n, 0, -1):
            if remaining[0] == 0:
                break
            if buckets[i].root.children:
                print(1)
                res.extend(buckets[i].get_word(buckets[i].root, '', remaining))
        return res
            
        
        