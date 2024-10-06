from collections import deque, defaultdict
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset = set(wordList)
        if endWord not in wordset:
            return []
        
        # BFS to build levels and parent-child relationship
        q = deque([beginWord])
        visited = set([beginWord])
        parents = defaultdict(list)  # to track parents of each word
        found = False
        level_words = set([beginWord])  # to track words at the current level

        while q and not found:
            next_level_words = set()
            for _ in range(len(q)):
                word = q.popleft()
                for i in range(len(word)):
                    for j in range(26):
                        new_word = word[:i] + chr(ord('a') + j) + word[i + 1:]
                        if new_word == endWord:
                            found = True
                        if new_word in wordset and new_word not in visited:
                            next_level_words.add(new_word)
                            parents[new_word].append(word)
                            
            visited.update(next_level_words)
            q.extend(next_level_words)

        if not found:
            return []

        # DFS to build the paths from endWord to beginWord
        res = []

        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for parent in parents[word]:
                dfs(parent, path + [parent])

        dfs(endWord, [endWord])
        return res
