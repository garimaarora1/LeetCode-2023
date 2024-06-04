class Solution:
    def partitionString(self, s: str) -> int:
        last_seen = defaultdict(int)
        substring_start_idx =  0
        count = 1
        for i in range(len(s)):
            if s[i] in last_seen and last_seen[s[i]] >= substring_start_idx:
                count += 1
                substring_start_idx = i
            last_seen[s[i]] = i 
        return count