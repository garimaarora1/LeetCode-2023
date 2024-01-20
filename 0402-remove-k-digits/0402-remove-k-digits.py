class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ms = []
        dup_k = k
        for i in num:
            while ms and i<ms[-1] and k:
                ms.pop()
                k -= 1
            ms.append(i)

        ans = ''.join(ms[0:len(num)-dup_k]).lstrip("0")
        return ans if ans else "0"
        