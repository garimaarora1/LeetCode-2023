class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i=0
        d={}
        for c in s1:
            d[c]=d.get(c,0)+1
        k=len(d) 
        j=0
        for i in range(len(s2)): 
            if s2[i] in d:
                d[s2[i]]-=1
                if d[s2[i]]==0:
                    k-=1
                    if k==0:
                        return True
            if i-j+1==len(s1):  
                if s2[j] in d:
                    d[s2[j]]+=1
                    if d[s2[j]]==1:
                        k+=1
                j+=1           
        return False