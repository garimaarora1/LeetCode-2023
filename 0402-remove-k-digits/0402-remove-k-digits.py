class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        attempts = k
        for n in num:
            while st and attempts and n < st[-1]:
                st.pop()
                attempts -= 1
            st.append(n)
        out = "".join(st[0:len(num)-k]).lstrip("0")
        return "0" if out == "" else out 