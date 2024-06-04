class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        t_len = len(t)
        count = 0
        for i in range(len(s)):
            if j == t_len:
                return count
            if s[i] == t[j]:
                j += 1
        if j < t_len:
            count += t_len-j
        return count
        