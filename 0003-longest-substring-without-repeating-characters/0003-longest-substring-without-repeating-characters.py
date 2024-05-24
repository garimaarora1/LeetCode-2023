class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        seen = set()
        max_length = 0
        while j < len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            max_length = max(max_length, len(seen))
            j += 1
        return max_length
            
                    
        