class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        modified_string = ''
        j = 0
        for i, ch in enumerate(s):
            
            if j < len(spaces) and i == spaces[j]:
                modified_string += ' '
                j += 1
            modified_string += ch
        return modified_string
            
        
        