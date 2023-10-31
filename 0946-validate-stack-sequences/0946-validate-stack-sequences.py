class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0 
        st = []
        for i in range(len(pushed)):
            st.append(pushed[i])
            while st and st[-1] == popped[j]:
                st.pop()
                j += 1
        while(j < len(popped)):
            if popped[j] != st[-1]:
                return False
            st.pop()
            j += 1
        return True