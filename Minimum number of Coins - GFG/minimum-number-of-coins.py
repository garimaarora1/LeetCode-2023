#User function Template for python3

class Solution:
    def minPartition(self, N):
        currency = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
        i = len(currency) - 1
        ans = []
        while N > 0:
            if currency[i]>N:
                i-=1
            else:
                while currency[i]<=N:
                    ans.append(currency[i])
                    N-=currency[i]
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends