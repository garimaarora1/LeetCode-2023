class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # Base case: if the string length is less than k, no valid substring can be formed
        if len(s) < k:
            return 0

        # Count the frequency of each character in the string
        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1

        # Find the first character that appears less than k times
        for char, freq in char_freq.items():
            if freq < k:
                # Split the string by this character and solve the problem for each substring
                return max(self.longestSubstring(sub, k) for sub in s.split(char))

        # If all characters appear at least k times, return the length of the string
        return len(s)
