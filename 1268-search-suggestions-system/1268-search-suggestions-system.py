class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end_of_word = False
        # self.word = None

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
        # curr.word = word

    def get_words_from_prefix(self, prefix, word):
        def dfs(curr, word, res):
            if len(res) == 3:
                return
            if curr.end_of_word == True:
                res.append(word)
            if not curr.children:
                return
            for i in range(26):
                ch  = chr(ord('a') + i)
                if ch not in curr.children:
                    continue
                dfs(curr.children[ch], word+ch, res)
        self.curr_prefix_node = self.curr_prefix_node.children[prefix]
        res = []
        dfs(self.curr_prefix_node, word, res)
        
        return res
        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie_obj = Trie()
        for product in products:
            trie_obj.insert_word(product)
        search_suggestions = []
        word = ''
        for ch in searchWord:
            word += ch
            search_suggestions.append(trie_obj.get_words_from_prefix(ch, word))
        
        return search_suggestions