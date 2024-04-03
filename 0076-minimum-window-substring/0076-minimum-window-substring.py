class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        maintain two dicts, 1. for freq of chars of t
        2. for freq for chars of s
        
        maintain two vars, have = 0, need = len(freq_t_dict)
        two vars for res, res_len
        
        loop over s 
        keep adding elements and count to freq_s_dict
        if char_freq_t[end] == char_freq_s[end]: have -= 1
        while have == need:
        1. update the res
        2. pop from window from left side
        """
        if t == "":
            return ""
        
        t_freq_dict, window_freq_dict = dict(), dict()
        
        for char in t:
            t_freq_dict[char] = t_freq_dict.get(char, 0) + 1
        
        have, need = 0, len(t_freq_dict)
        res, res_len = [-1,-1], float("infinity")
        start = 0
        for end in range(len(s)):
            char = s[end]
            window_freq_dict[char] = window_freq_dict.get(char, 0) + 1
            
            if char in t_freq_dict and t_freq_dict[char] == window_freq_dict[char]:
                have += 1
            
            while have == need:
                # update the res 
                if end - start + 1 < res_len:
                    res_len = end - start + 1
                    res = [start, end]
                
                # pop from the left of window
                window_freq_dict[s[start]] -= 1
                if s[start] in t_freq_dict and window_freq_dict[s[start]] < t_freq_dict[s[start]]:
                    have -= 1
                start += 1
        start, end = res
        return s[start:end+1] if res_len != float("infinity") else ""