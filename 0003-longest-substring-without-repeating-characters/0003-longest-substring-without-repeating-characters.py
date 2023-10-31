class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        curr_sub_string_len = 0
        max_sub_string_len = 0 
        j = 0
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
            # new ele got added to dict 
            if d[s[i]] == 1:
                curr_sub_string_len += 1
                max_sub_string_len = max(max_sub_string_len, curr_sub_string_len)
            # duplicate ele got added to dict
            else:
                while d[s[i]] >1:
                    d[s[j]] -= 1
                    if d[s[j]] == 0:
                        curr_sub_string_len -= 1
                    j += 1
        return max_sub_string_len
        