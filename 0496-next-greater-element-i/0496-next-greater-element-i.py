class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        st = []
        d = {}
        for i in range(len(nums2)-1, -1, -1):
            while st and st[-1] <= nums2[i]:
                st.pop()
            if not st:
                d[nums2[i]] = -1
            elif st and st[-1] > nums2[i]:
                d[nums2[i]] = st[-1]
            st.append(nums2[i])
        
        for num in nums1:
            ans.append(d[num])
        return ans