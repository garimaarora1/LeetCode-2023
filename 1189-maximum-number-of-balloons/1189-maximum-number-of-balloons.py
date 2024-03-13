class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ballon_freq_dict = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        count = len(text)
        text_freq_dict = defaultdict(int)
        for char in text:
            text_freq_dict[char] += 1
        for char in ballon_freq_dict:
            if text_freq_dict[char] == 0:
                return 0
            else:
                count = min(count, text_freq_dict[char] // ballon_freq_dict[char])
        return count
        
        