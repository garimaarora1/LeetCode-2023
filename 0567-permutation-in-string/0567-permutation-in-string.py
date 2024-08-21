class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i, j = 0, 0
        counter = Counter(s1)
        unique_characters = len(counter)
        
        while j < len(s2):
            if s2[j] in counter:
                counter[s2[j]] -= 1
                if counter[s2[j]] == 0:
                    unique_characters -= 1
                if unique_characters == 0:
                    return True
            if j-i+1 == len(s1):
                if s2[i] in counter:
                    counter[s2[i]] += 1
                    if counter[s2[i]] == 1:
                        unique_characters += 1
                i += 1
            j += 1
        return False
            
                
        
        