class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        res = ''
        for ch in order:
            if ch in s:
                if counter[ch] > 0:
                    res += ch*counter[ch]
                    counter[ch] = 0
        for key in counter:
            if counter[key] > 0:
                res += key * counter[key]
                counter[key] = 0
        return res
                
        