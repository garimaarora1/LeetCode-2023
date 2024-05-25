class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        unique_chars = len(counter)
        i = j = 0
        mini = float('inf')
        res = []
        while j < len(s):
            ch = s[j]
            if ch in counter:
                counter[ch] -= 1
                if counter[ch] == 0:
                    unique_chars -= 1
            while unique_chars == 0 and i <= j:
                if j-i+1 < mini:
                    mini = j-i+1
                    res = (i,j)
                if s[i] in counter:
                    counter[s[i]] += 1
                    if counter[s[i]] == 1:
                        unique_chars += 1
                i += 1
            j += 1
        return "" if mini== float('inf') else s[res[0]:res[1]+1]