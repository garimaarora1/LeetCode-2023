class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        s = 0
        e = len(a)-1
        while s < e:
            if a[s] + a[e] == target:
                return s+1, e+1
            if a[s] + a[e] > target:
                e-=1
            else:
                s+=1