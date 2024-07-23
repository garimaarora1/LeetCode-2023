class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.end_of_word
            
            ch = word[i]
            if ch == '.':
                for child in node.children:
                    if dfs(node.children[child], i + 1):
                        return True
                return False
            else:
                if ch in node.children:
                    return dfs(node.children[ch], i + 1)
                else:
                    return False

        return dfs(self.root, 0)

# Example usage:
# obj = WordDictionary()
# obj.addWord("word")
# print(obj.search("word"))   # Output: True
# print(obj.search("wor."))   # Output: True
# print(obj.search("wo.d"))   # Output: True
# print(obj.search("wo.."))   # Output: True
# print(obj.search("wordd"))  # Output: False
