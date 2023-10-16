from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(int)
        res = []
        for i in nums1:
            d[i] += 1

        for i in nums2:
            if d.get(i):
                res.append(i)
                d[i] -= 1
        return res
            
        