from collections import deque
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        q = deque([(0, "")])
        res = []
        
        while q:
            start_index, current_sentence = q.popleft()
            
            if start_index == len(s):
                res.append(current_sentence.strip())
                continue
            
            for end_index in range(start_index + 1, len(s) + 1):
                word = s[start_index:end_index]
                if word in word_set:
                    new_sentence = current_sentence + " " + word
                    q.append((end_index, new_sentence))
        
        return res
