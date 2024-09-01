class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        n = len(s)

        # find max freq ch, and max freq
        max_count = 0
        max_freq_ch = ''
        
        for char, value in counter.items():
            if value > max_count:
                max_count = value
                max_freq_ch = char
        
        if max_count > (n + 1) // 2:
            return ''
        
        ans = [''] * n 
        i = 0
        
        # place max freq ch alternatively
        while counter[max_freq_ch] != 0:
            ans[i] = max_freq_ch
            counter[max_freq_ch] -= 1
            i += 2
        
        # place rest of the chars in any order
        for ch, count in counter.items():
            while count != 0:
                if i >= n:
                    i = 1
                ans[i] = ch
                count -= 1
                i += 2
        return ''.join(ans)
                