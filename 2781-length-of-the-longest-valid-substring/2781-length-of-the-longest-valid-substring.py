class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden_set = set(forbidden)
        i = j = 0
        max_length = 0
        while j < len(word):
            k = j
            while k >= max(i, j-10):
                if word[k:j+1] in forbidden_set:
                    i = k + 1
                    break
                k -= 1
            max_length = max(max_length,j-i+1)
            j += 1
        return max_length
        
