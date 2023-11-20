class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        mini = float('inf')
        dict = {}
        for i,word in enumerate(wordsDict):
            if word in dict:
                dict[word].append(i)
            else:
                dict[word] = [i]
        for v1 in dict[word1]:
            for v2 in dict[word2]:
                mini = min(mini, abs(v1-v2))
        return mini