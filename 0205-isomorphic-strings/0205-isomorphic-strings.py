class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_dict = defaultdict(str)
        for i in range(len(s)):
            if s[i] not in map_dict:
                if t[i] in map_dict.values():
                    return False
                map_dict[s[i]] = t[i]
                
            else:
                if map_dict[s[i]] != t[i]:
                    return False
        return True
    
        
        