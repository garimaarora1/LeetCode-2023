class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = j = 0 
        counter = defaultdict(int)
        maxi = 0
        while j < len(s):
            counter[s[j]] += 1
            max_freq = max(counter.values())
            
            while (j-i+1) - max(counter.values()) > k:
                counter[s[i]] -= 1
                i += 1
            maxi = max(maxi, j-i+1)
            j += 1
        return maxi
                
            
        