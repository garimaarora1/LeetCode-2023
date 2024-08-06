class Solution:
    def minimumPushes(self, word: str) -> int:
        
        """
        word 
        8 keys
        26 characters
        
        3*6 = 18 
        4*2 = 8: 
        
        freq: counter(word)
        
        get values in reverse sorted order 
        
        key  = 0
        row = 0
        
        if key == 9:
        row += 1
        coutn += row * freq
        """
        freq_map = Counter(word)
        sorted_freq = sorted(freq_map.values(), reverse=True)
        key, row = 0, 0
        min_count = 0
        for freq in sorted_freq:
            row = (key // 8) + 1
            min_count += row * freq
            key += 1
        return min_count
            
        
        