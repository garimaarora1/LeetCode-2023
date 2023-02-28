#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
        i = 0
        subarr = []
        res = []
        def fun(arr, i, subarr):
            if i == len(arr):
                res.append(sum(subarr))
                return 
            subarr.append(arr[i])    
            fun(arr, i+1, subarr)
            subarr.pop()
            fun(arr, i+1,subarr)
        fun(arr, i, subarr)
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends