#User function Template for python3

class Solution:

	def search(self,pat, txt):
        d = {}
        ans = 0
        for i in range(len(pat)):
            d[pat[i]] = d.get(pat[i],0) + 1
        i, j = 0, 0
        c = len(d)
        
        while j<len(txt):
            if txt[j] in d:
                d[txt[j]] -= 1

                if d[txt[j]] == 0:
                    c -= 1

            if j-i+1 < len(pat):
                j += 1
            else: 
                if c == 0:
                    ans += 1

                if txt[i] in d:
                    d[txt[i]] += 1
                    if d[txt[i]] == 1:
                        c += 1

                i += 1
                j += 1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code Ends