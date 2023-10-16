from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        res = []
        for i in nums1:
            d1[i] += 1
        for i in nums2:
            d2[i] += 1
        for key in d1:
            if key in d2:
                val = min(d1[key], d2[key])
                sub_list = val*[key]
                res.extend(sub_list)
        return res
            
        