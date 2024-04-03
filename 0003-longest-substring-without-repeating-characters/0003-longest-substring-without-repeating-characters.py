class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maximum_window_len = 0 
        unique_char_set = set()
        for end in range(len(s)):
            while s[end] in unique_char_set:
                unique_char_set.remove(s[start])
                start += 1
            unique_char_set.add(s[end])
            maximum_window_len = max(maximum_window_len, end-start+1)
        return maximum_window_len

