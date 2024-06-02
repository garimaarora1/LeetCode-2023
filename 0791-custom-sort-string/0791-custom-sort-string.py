class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        res = ''
        for ch in order:
            if counter[ch] > 0:
                res += ch*counter[ch]
                counter[ch] = 0
        for key,value in counter.items():
            if counter[key] > 0:
                res += key * value
        return res
                
        