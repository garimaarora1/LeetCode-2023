class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [i, 1]
            else:
                d[s[i]][1] += 1
                
        for key in d:
            if d[key][1] == 1:
                return d[key][0]
        return -1
        
        