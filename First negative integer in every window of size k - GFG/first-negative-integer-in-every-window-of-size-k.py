#User function Template for python3

def printFirstNegativeInteger(a, n, k):
    l = []
    ans = []
    i, j = 0, 0
    while j < n:
        if a[j] < 0:
            l.append(a[j])
        if j-i + 1 < k:
            j += 1
        else: 
            if l:
                ans.append(l[0])
                if l[0] == a[i]:
                    l.pop(0)
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