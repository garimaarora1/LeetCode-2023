class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        q.append((beginWord,1))
        s=set(wordList)
        if endWord not in wordList:
            return 0
        visited=set()
        visited.add(beginWord)
        while q:
            word,c=q.popleft()
            if word==endWord:
                return c
            for i in range(len(word)):
                for j in range(26):
                    newWord=word[:i]+chr(ord('a')+j)+word[i+1:]
                    if  newWord in s and newWord not in visited:
                        q.append((newWord,c+1))
                        visited.add(newWord)
        return 0