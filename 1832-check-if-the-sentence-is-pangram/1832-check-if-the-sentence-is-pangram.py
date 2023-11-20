class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set()
        for char in sentence:
            if char >= 'a' and char <= 'z' and char.lower() not in s:
                s.add(char)
        return len(s) == 26