class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end_of_word = True

    def get_words(self, node: TrieNode, prefix: str, k: int) -> List[str]:
        if k[0] == 0:
            return []
        res = []
        if node.end_of_word:
            k[0] -= 1
            res.append(prefix)
        for c in sorted(node.children.keys()):  # Sort keys to get words in lexicographical order
            res += self.get_words(node.children[c], prefix + c, k)
        return res

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        n = len(words)
        cnt = Counter(words)
        bucket = [Trie() for _ in range(n+1)]
        self.k = k

        def add_word(trie: Trie, word: str) -> None:
            trie.add_word(word)

        def get_words(trie: Trie, prefix: str) -> List[str]:
            return trie.get_words(trie.root, prefix, [self.k])

        for word, freq in cnt.items():
            add_word(bucket[freq], word)

        res = []
        for i in range(n, 0, -1):
            if self.k == 0:
                return res
            if bucket[i].root.children:
                res += get_words(bucket[i], '')
        return res[:self.k]  # Ensure we only return the top k results
