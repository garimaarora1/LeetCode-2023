#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        c = 1
        time = [[start[i],end[i]] for i in range(n)]
        time.sort(key=lambda x:x[1])
        s1, e1 = time[0][0], time[0][1]
        for t in time[1:]:
            s2, e2 = t[0], t[1]
            if s2 > e1:
                c += 1
                s1, e1 = s2, e2
        return c
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends