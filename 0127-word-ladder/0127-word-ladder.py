class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        queue.append((beginWord,1))
        seen = set(wordList)

        if endWord not in wordList:
            return 0

        visited = set()
        visited.add(beginWord)

        while queue:
            word, ch = queue.popleft()
            if word == endWord:
                return ch

            for i in range(len(word)):
                for j in range(26):
                    newWord = word[:i] + chr(ord('a') + j) + word[i+1:]
                    if newWord in seen and newWord not in visited:
                        queue.append((newWord, ch+1))
                        visited.add(newWord)
        return 0