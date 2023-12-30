class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = defaultdict(int)
        l = len(words)
        for word in words:
            for i in word:
                d[i] += 1
        for key in d:
            if d[key] % l != 0:
                return False
        return True