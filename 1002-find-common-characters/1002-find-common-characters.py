class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        master_counter = defaultdict(int)
        res = []
        
        for ch in words[0]:
            master_counter[ch] += 1
            
        for word in words[1:]:
            curr_counter = defaultdict(int)
            for ch in word:
                curr_counter[ch] += 1
            for ch in master_counter:
                master_counter[ch] = min(master_counter[ch], curr_counter[ch])
        
        for ch, freq in master_counter.items():
            for i in range(freq):
                res.append(ch)
        return res