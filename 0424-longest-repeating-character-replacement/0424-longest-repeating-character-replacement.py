class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0
        freq = defaultdict(int)
        max_length = 0
        while j < len(s):
            freq[s[j]] += 1
            max_freq = max(freq.values())
            while j-i+1 - max(freq.values()) > k:
                freq[s[i]] -= 1
                i += 1
            max_length = max(max_length, j-i+1)
            j += 1
        return max_length