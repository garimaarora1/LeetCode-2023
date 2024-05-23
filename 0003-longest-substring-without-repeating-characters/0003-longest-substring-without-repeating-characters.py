class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i = j = 0
        max_length = 0
        while j < len(s):
            if s[j] not in seen:
                max_length = max(max_length, j-i+1)
            else:
                while s[j] in seen:
                    seen.remove(s[i])
                    i += 1
            seen.add(s[j])
            j += 1
        return max_length
                
                
            
        