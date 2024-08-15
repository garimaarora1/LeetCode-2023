class TrieNode:
    def __init__(self):
        self.word = None
        self.child = defaultdict(TrieNode)

    def addWord(self, word):
        curr = self
        for c in word:
            curr = curr.child[c]
        curr.word = word

    def getWords(self, limit):
        words = []

        def dfs(curr):
            if len(words) == limit: return
            if curr.word != None:
                words.append(curr.word)
            for c in sorted(curr.child.keys()):
                if c in curr.child:
                    dfs(curr.child[c])

        dfs(self)
        return words

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        for product in products:
            root.addWord(product)

        ans = []
        curr = root
        for c in searchWord:
            if curr != None and c in curr.child:
                curr = curr.child[c]
                ans.append(curr.getWords(3))
            else:
                curr = None
                ans.append([])
        return ans