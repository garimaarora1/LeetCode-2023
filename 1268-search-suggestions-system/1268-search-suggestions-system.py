class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end_of_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.curr_prefix_node = self.root
    
    def insert_word(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end_of_word = True
        curr.word = word

    def get_words_from_prefix(self, prefix):
        def dfs(curr, res):
            if len(res) == 3:
                return res
            if curr.end_of_word == True:
                res.append(curr.word)
            for i in range(26):
                ch  = chr(ord('a') + i)
                if ch not in curr.children:
                    continue
                dfs(curr.children[ch], res)
        self.curr_prefix_node = self.curr_prefix_node.children[prefix]
        curr = self.curr_prefix_node
        res = []
        dfs(curr, res)
        
        return res
        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie_obj = Trie()
        for product in products:
            trie_obj.insert_word(product)
        search_suggestions = []
        for ch in searchWord:
            search_suggestions.append(trie_obj.get_words_from_prefix(ch))
        
        return search_suggestions