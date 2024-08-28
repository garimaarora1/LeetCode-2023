class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        isomorphic_map = defaultdict(str)
        
        for i in range(len(s)):
            if s[i] not in isomorphic_map:
                if t[i] in isomorphic_map.values():
                    return False
                isomorphic_map[s[i]] = t[i]
            else:
                if isomorphic_map[s[i]] != t[i]:
                    return False
        return True