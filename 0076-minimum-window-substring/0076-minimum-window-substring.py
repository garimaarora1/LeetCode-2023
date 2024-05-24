class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d=Counter(t)
        req=len(d)
        mini=float('inf')
        res=[]
        j=0
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]-=1
                if d[s[i]]==0:
                    req-=1
            while req==0 and j<len(s):
                if i-j+1<mini:
                    res=[j,i]
                    mini=i-j+1
                if s[j] in d:
                    d[s[j]]+=1
                    if d[s[j]]==1:
                        req+=1
                j+=1
        return "" if mini== float('inf') else s[res[0]:res[1]+1]