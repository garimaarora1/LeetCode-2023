class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_array = [0] * 26
        for char in s:
            freq_array[ord(char)-97] += 1
        for char in t:
            val = freq_array[ord(char)-97]
            if val == 0:
                return False
            freq_array[ord(char)-97] -= 1
        return True
            

        