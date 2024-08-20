class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = Counter(t)
        unique_ch = len(counter_t)
        i, j = 0, 0
        mini = float('inf')
        res = []
        while j < len(s):
            if s[j] in counter_t:
                counter_t[s[j]] -= 1
                if counter_t[s[j]] == 0:
                    unique_ch -= 1
            
            while unique_ch == 0 and i <= j:
                if j-i+1 < mini:
                    mini = j-i+1
                    res = [i, j]
                
                if s[i] in counter_t:
                    counter_t[s[i]] += 1
                    if counter_t[s[i]] == 1:
                        unique_ch += 1
                i += 1
            j += 1
        return "" if mini == float('inf') else s[res[0]:res[1]+1]
                
        
        
        