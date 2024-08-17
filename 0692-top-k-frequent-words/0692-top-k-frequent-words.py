from collections import Counter

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end_of_word = True

    def get_words(self, node, prefix, remaining):
        if remaining[0] == 0:
            return []
        res = []
        if node.end_of_word:
            remaining[0] -= 1
            print(prefix)
            res.append(prefix)

        for i in range(26):
            c = chr(ord('a') + i)
            if c in node.children:
                res += self.get_words(node.children[c], prefix + c, remaining)
        return res

class Solution:
    def topKFrequent(self, words, k):
        n = len(words)
        cnt = Counter(words)
        bucket = [Trie() for _ in range(n + 1)]
        
        for word, freq in cnt.items():
            bucket[freq].add_word(word)
        
        res = []
        
        for i in range(n, 0, -1):
            if k == 0:
                break
            if bucket[i].root.children:
                remaining = [k]
                words_from_bucket = bucket[i].get_words(bucket[i].root, '', remaining)
                res.extend(words_from_bucket)
                k = remaining[0]
        
        return res