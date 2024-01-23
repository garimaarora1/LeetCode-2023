class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter_dict = defaultdict(int)
        longest_len = 0
        flag = False
        for ch in s:
            counter_dict[ch] += 1
        
        for key in counter_dict:
            value = counter_dict[key]
            if value % 2 == 0:
                longest_len += value
            else:
                longest_len += value - 1
                if not flag:
                    longest_len += 1
                    flag = True
        return longest_len
                
                
                
        