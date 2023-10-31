class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        K=k
        for n in num:
            while st and k and n < st[-1]:
                st.pop()
                k -= 1
            st.append(n)
        out = "".join(st[0:len(num)-K]).lstrip("0")
        return "0" if out == "" else out 