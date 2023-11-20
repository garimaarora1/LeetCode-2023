class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        mini = len(wordsDict)
        p1, p2 = -1, -1
        for i, word in enumerate(wordsDict):
            if word == word1:
                p1 = i
            elif word == word2:
                p2 = i
            if p1 != -1 and p2 != -1:
                mini = min(mini, abs(p1-p2))
        return mini
                
 