class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = defaultdict(int)
        for ch in s1:
            counter[ch] += 1
        unique_ch = len(counter)
        i, j = 0, 0
        while j < len(s2):
            ch = s2[j]
            if ch in counter:
                counter[ch] -= 1
                if counter[ch] == 0:
                    unique_ch -= 1
                
                if unique_ch == 0:
                    return True
            
            if j-i+1 == len(s1):
                if s2[i] in counter:
                    counter[s2[i]] += 1
                    if counter[s2[i]] == 1:
                        unique_ch += 1
                    
                i += 1
            j += 1
        return False
                
        