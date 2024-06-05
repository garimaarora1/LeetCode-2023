class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        i, j = 0, 0
        forbidden_set = set(forbidden)
        max_length = 0
        while j < len(word):
            k = j
            while k >= max(i, j-10):
                if word[k:j+1] in forbidden_set:
                    i = k + 1
                    break
                k -= 1
            
            max_length = max(max_length, j-i+1)
            j += 1
        return max_length
        