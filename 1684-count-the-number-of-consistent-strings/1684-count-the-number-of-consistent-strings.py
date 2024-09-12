class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        count = 0
        
        for word in words:
            consider = True
            for ch in word:
                if ch not in allowed_set:
                    consider = False
                    break
            if consider:
                count += 1
        return count