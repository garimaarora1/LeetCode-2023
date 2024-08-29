class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0
        freq_map = defaultdict(int)
        maxi = 0
        while j < len(s):
            freq_map[s[j]] += 1
            
            while (j-i+1) - max(freq_map.values()) > k:
                freq_map[s[i]] -= 1
                i += 1
            maxi = max(maxi, j-i+1)
            j += 1
        return maxi