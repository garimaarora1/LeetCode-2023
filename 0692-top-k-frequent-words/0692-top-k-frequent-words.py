from collections import Counter
from typing import List

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

    def get_words(self, node: TrieNode, prefix: str, remaining: List[int]) -> List[str]:
        if remaining[0] == 0:
            return []
        res = []
        if node.end_of_word:
            remaining[0] -= 1
            print(prefix)
            res.append(prefix)
        for c in sorted(node.children.keys()):  # Sort to ensure lexicographical order
            res += self.get_words(node.children[c], prefix + c, remaining)
        return res
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        n = len(words)
        cnt = Counter(words)
        bucket = [Trie() for _ in range(n + 1)]
        
        # Add words to corresponding frequency buckets
        for word, freq in cnt.items():
            bucket[freq].add_word(word)
        
        res = []
        
        # Process buckets in reverse order
        for i in range(n, 0, -1):
            if k == 0:
                break
            if bucket[i].root.children:
                remaining = [k]  # Use a list to allow modification inside get_words
                words_from_bucket = bucket[i].get_words(bucket[i].root, '', remaining)
                res.extend(words_from_bucket)
                k = remaining[0]  # Update k to reflect how many more words are needed
        
        # Return the top k words, ensuring only the top k are included
        return res[:len(res)]  # Ensure to return the exact number of collected words
