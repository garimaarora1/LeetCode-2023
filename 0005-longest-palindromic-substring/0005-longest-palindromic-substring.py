class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        max_length = 0
        indices = None
        for mid in range(length):
            for j in range(mid, mid+2):
                right = j
                left = mid
                while left >= 0 and right <= length-1 and s[left] == s[right]:
                    if right - left + 1 > max_length:
                        max_length = right - left + 1
                        indices = [left, right]
                    left -= 1
                    right += 1

        return s[indices[0]:indices[1]+1]

            
        