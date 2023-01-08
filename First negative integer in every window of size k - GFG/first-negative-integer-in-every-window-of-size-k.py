#User function Template for python3
from collections import deque
def printFirstNegativeInteger(a, n, k):
    d = deque()
    ans = []
    i, j = 0, 0
    while j < n:
        if a[j] < 0:
            d.append(a[j])
        if j-i + 1 < k:
            j += 1
        else: 
            if d:
                ans.append(d[0])
                if d[0] == a[i]:
                    d.popleft()
            else:
                ans.append(0)
            i += 1
            j += 1
    return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends