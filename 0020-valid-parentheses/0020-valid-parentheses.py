class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_dict = {')': '(', '}': '{', ']': '[' }
        st = []
        
        for char in s:
            if char in parentheses_dict.values():
                st.append(char)
            else:
                if st and st[-1] == parentheses_dict[char]:
                    st.pop()
                else:
                    return False
        return True if not st else False