#User function Template for python3
from collections import defaultdict
class Solution:

    def longestKSubstr(self, s, k):
        # code here
        i, j = 0, 0
        maxi = -1
        d = defaultdict(int)
        while j < len(s):
            d[s[j]] += 1
            if len(d) < k:
                j += 1
            elif len(d) == k:
                maxi = max(maxi, j-i+1)
                j += 1
            elif len(d) > k:
                while s[i]==s[i+1]:
                    d[s[i]] -= 1
                    i += 1
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    del d[s[i]]
                i += 1
                j += 1

        return maxi

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends