class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_list_set = set(wordList)
        if endWord not in wordList:
            return 0
        queue = deque()
        visited = set()
        queue.append(beginWord)
        count = 1
        while queue:
            count += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(len(word)):
                    for k in range(ord("a"), ord("z")+1):
                        new_word = word[:i] + chr(k) + word[i+1:]
                        if new_word == endWord:
                            return count
                        if new_word in word_list_set:
                            queue.append(new_word)
                            word_list_set.remove(new_word)
        return 0
                    
            
        