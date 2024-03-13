class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        st = []
        for i in range(len(nums2)-1, -1, -1):
            while st and st[-1] <= nums2[i]:
                st.pop()
            if not st:
                ans.append(-1)
            elif st and st[-1] > nums2[i]:
                ans.append(st[-1])
            st.append(nums2[i])
        ans = ans[::-1]
        
        final_ans = []
        for num in nums1:
            i = nums2.index(num)
            final_ans.append(ans[i])
        return final_ans