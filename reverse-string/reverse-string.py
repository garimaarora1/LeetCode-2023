class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        def fun(s, i):
            if s == [] or i == len(s)//2:
                return
            s[i], s[n-i-1] = s[n-i-1], s[i]
            fun(s, i+1)
        fun(s, 0)