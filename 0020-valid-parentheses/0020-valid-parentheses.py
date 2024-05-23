class Solution:
    def isValid(self, s: str) -> bool:
        valid_parantheses = {'(': ')', '{': '}', '[': ']'}
        st = []
        for para in s:
            if para in list(valid_parantheses.keys()):
                st.append(para)
            else:
                if not st:
                    return False
                ele = st.pop()
                if valid_parantheses[ele] != para:
                    return False
        return st==[]
        