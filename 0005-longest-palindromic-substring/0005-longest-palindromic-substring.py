class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        max_palindrome_length = 0
        indexes = None
        for i in range(length):
            mid = i
            for j in range(mid, mid+2):
                left = mid
                right = j
                
                while left >= 0 and right <= length-1 and s[left] == s[right]:
                    if right - left + 1 > max_palindrome_length:
                        max_palindrome_length = right - left + 1
                        indexes = [left, right]
                    left -= 1
                    right += 1
        return s[indexes[0]:indexes[1]+1]