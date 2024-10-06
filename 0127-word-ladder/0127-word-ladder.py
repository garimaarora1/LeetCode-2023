class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([beginWord])
        s = set(wordList)
        
        if endWord not in wordList:
            return 0
        
        steps = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                for i in range(len(word)):
                    for j in range(26):
                        newWord = word[:i] + chr(ord('a') + j) + word[i+1:]
                        if newWord == endWord:
                            return steps + 1
                        if newWord in s:
                            q.append(newWord)
                            s.remove(newWord)
            steps += 1
        
        return 0
