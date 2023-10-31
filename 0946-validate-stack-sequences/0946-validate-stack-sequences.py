class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0 
        st = []
        for i in range(len(pushed)):
            st.append(pushed[i])
            while st and st[-1] == popped[j] and j < len(popped):
                st.pop()
                j += 1
        return j == len(popped)