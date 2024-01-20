class Solution:
    def removeDuplicates(self, s: str) -> str:
        ms = []
        for i in s:
            if ms and ms[-1] == i:
                while ms and ms[-1] == i:
                    ms.pop()
            else:
                ms.append(i)
        return ''.join(ms)
            
                
            
        