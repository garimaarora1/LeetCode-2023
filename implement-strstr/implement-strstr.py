class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
            i=0
            j=0
            n=len(haystack)
            while(i<n):
                k=i
                while(k<n and haystack[k]==needle[j]):
                    j+=1
                    k+=1
                    if j==len(needle):
                        return i
                else:
                    j=0
                    i+=1
            return -1