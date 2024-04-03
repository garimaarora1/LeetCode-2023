class Solution:
    def characterReplacement(self, s: str, k: int) -> int: 
        start = 0
        max_char_freq = 0
        count_freq = dict()
        for end in range(len(s)):
            count_freq[s[end]] = count_freq.get(s[end], 0) + 1
            max_char_freq = max(max_char_freq, count_freq[s[end]])
            
            if (end-start+1) - max_char_freq > k:
                count_freq[s[start]] -= 1
                start += 1
        return end-start+1
        
            
