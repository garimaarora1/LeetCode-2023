class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = defaultdict(int)
        maxi = -1
        for i, ch in enumerate(s):
            ch_pos = d.get(ch)
            if ch_pos is not None:
                maxi = max(maxi, i-ch_pos-1)
            else:
                d[ch] = i
        return maxi
                