class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
   
        charMap = {}
        for char in text:
            if char in "balloon":
                if char not in charMap:
                    charMap[char] = 1
                else:
                    charMap[char] += 1

        for char in "balloon":
            if char not in charMap:
                return 0

        charMap["l"] //= 2
        charMap["o"] //= 2

        minChar = len(text)

        for char in charMap:
            if (charMap[char] < minChar):
                minChar = charMap[char]

        return minChar