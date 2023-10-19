class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        l = len(strs[0])
        if l == 0:
            return ''
        for i in range(len(strs)):
            j = 0 
            while j < len(strs[i]) and l > j and strs[i][j] == strs[0][j]:
                j += 1
            l = min(l, j)
        return strs[0][:l]
        