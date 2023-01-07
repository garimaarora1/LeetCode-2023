class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        t=0
        c=0
        s=0
        for i in range(n):
            t+=gas[i]-cost[i]
            c+=gas[i]-cost[i]
            if c<0:
                s=i+1
                c=0
        return s if t>=0 else -1
