class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_palindrome_len = 0
        indexes = None
        for i in range(n):
            mid = i
            for j in range(i, i+2):
                left = mid
                right = j
                
                while left>=0 and right<=n-1 and s[left] == s[right]:
                    if right - left + 1 > max_palindrome_len:
                        max_palindrome_len = right - left + 1
                        indexes = [left, right]
                    left -= 1
                    right += 1
        return s[indexes[0]: indexes[1]+1]