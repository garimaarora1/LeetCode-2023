class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_dict = defaultdict(int)
        for ch in magazine:
            counter_dict[ch] += 1
        for ch in ransomNote:
            if counter_dict[ch] == 0:
                return False
            counter_dict[ch] -= 1
            
        return True
        
        
        