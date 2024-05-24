class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = defaultdict(int)
        for ch in s1:
            counter[ch] += 1
        window_size = len(s1)
        i = j = 0
        count = 0
        while j < len(s2):
            ch = s2[j]
            if ch in counter:
                counter[ch] -= 1
                
                if counter[ch] == 0:
                    count += 1
                if j - i + 1 == window_size and count == len(counter):
                    return True
            if j - i + 1 == window_size:
                if s2[i] in counter:
                    counter[s2[i]] += 1
                    if counter[s2[i]] == 1:
                        count -= 1
                i += 1 
            j += 1
            
        return False