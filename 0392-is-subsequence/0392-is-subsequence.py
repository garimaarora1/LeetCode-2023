class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        s_len = len(s)
        t_len = len(t)

        if len(s) > len(t): 
            return False      

        i = 0
        for j in range(len(t)):
            if t[j] == s[i]:
                i += 1
            
            if i == s_len:
                return True
        return False