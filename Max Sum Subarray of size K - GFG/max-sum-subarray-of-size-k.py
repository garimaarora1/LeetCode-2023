#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        i, j, maxi, s = 0, 0, -1000000, 0
        while j <= N-1:
            if j < K-1:
                s += Arr[j]
            elif j-i+1 == K:
                s += Arr[j]
                maxi = max(s, maxi)
            else:
                s = s - Arr[i] + Arr[j]
                maxi = max(s, maxi)
                i += 1
            j+=1
        return maxi

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends