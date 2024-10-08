class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordlist_set = set(wordList)
        if endWord not in wordlist_set:
            return []
        queue = deque([beginWord])
        visited = set(beginWord)
        parents = defaultdict(list)
        found = False

        while queue and not found:
            next_level_set = set()
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(len(word)):
                    for j in range(26):
                        new_word = word[:i] + chr(ord('a') + j) + word[i+1:]
                    
                        if new_word == endWord:
                            found = True
                        if new_word in wordlist_set and new_word not in visited:
                            next_level_set.add(new_word)
                            parents[new_word].append(word)
            visited.update(next_level_set)
            queue.extend(next_level_set)
        
        if not found:
            return []

        res = []
        
        # backtracking
        def dfs(node, curr_path):
            if node == beginWord:
                res.append(curr_path[::-1])
                return
            
            for parent in parents[node]:
                dfs(parent, curr_path + [parent])
        dfs(endWord, [endWord])
        
        return res