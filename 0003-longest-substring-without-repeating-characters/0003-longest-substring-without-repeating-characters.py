class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        curr_window_len = 0
        maximum_window_len = 0 
        unique_char_set = set()
        i = 0
        while i < len(s):
            while s[i] in unique_char_set and start < end:
                unique_char_set.remove(s[start])
                start += 1
            unique_char_set.add(s[i])
            end += 1
            i += 1
            curr_window_len = max(curr_window_len, len(unique_char_set))
            maximum_window_len = max(maximum_window_len, curr_window_len)
        return maximum_window_len

