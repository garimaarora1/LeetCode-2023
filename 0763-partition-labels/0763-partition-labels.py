class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        idx_map = defaultdict(int)
        
        for i, ch in enumerate(s):
            idx_map[ch] = i

        res = []
        
        i = 0
        j = 0
        k = 0
        while i < len(s) and j < len(s):
            ch = s[j]
            last_idx = idx_map[ch]
            k = max(k, last_idx)
            if j == k:
                res.append(j-i+1)
                i = j + 1
            j += 1

        return res
            
            
            
            
                
        