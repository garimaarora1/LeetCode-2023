class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        maxi = 0
        i = 0
        for j in range(len(s)):
            d[s[j]] += 1

            while (j-i+1 - max(d.values())) >k:
                d[s[i]] -= 1
                i += 1
            maxi = max(maxi, j-i+1)

        return maxi
