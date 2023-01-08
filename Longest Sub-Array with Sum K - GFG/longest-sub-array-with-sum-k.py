#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, a, n, k) : 
        #Complete the function
        maxi = 0
        s = 0
        d = {}
        for i in range(n):
            s += a[i]
            if s == k:
                maxi = i + 1
            if s not in d:
                d[s] = i
            if s-k in d:
                maxi = max(maxi, i-d[s-k])
                
        return maxi
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends