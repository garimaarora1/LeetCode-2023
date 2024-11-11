class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        word_list_set = set(wordList)
        if endWord not in word_list_set:
            return 0

        queue = deque([beginWord])
        steps = 1
    
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(len(word)):
                    for j in range(26):
                        new_word = word[:i] + chr(ord('a') + j) + word[i+1:]
                        if new_word == endWord:
                            return steps + 1
                        if new_word in word_list_set:
                            queue.append(new_word)
                            word_list_set.remove(new_word)
            steps += 1
        
        return 0