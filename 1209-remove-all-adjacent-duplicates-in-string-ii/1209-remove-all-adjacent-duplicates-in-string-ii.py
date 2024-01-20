class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        ms = []
        ans = []
        for i in s:
            if ms and ms[-1][0] == i and ms[-1][1] == k-1:
                while ms and ms[-1][0] == i and ms[-1][1] <= k-1:
                    ms.pop()
            elif ms and ms[-1][0] == i:
                ms.append((i,ms[-1][1]+1))
            else:
                ms.append((i, 1))
        for item in ms:
            ans.append(item[0])
        return ''.join(ans)
            
                
                
            