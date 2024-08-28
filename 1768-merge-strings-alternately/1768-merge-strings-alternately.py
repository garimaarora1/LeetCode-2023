class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        res = ''
        for i in range(max(len1,len2)):
            if i < len1:
                res += word1[i]
            if i < len2:
                res += word2[i]
        return res