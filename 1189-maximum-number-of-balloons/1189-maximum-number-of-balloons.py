class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ballon_dict = {'b': 1, 'a': 1, 'l': 2, 'o':2, 'n': 1}
        counter_dict = defaultdict(int)
        count = len(text)
        for char in text:
            counter_dict[char] += 1
        for char in ballon_dict:
            if counter_dict[char] == 0:
                return 0
            else:
                count = min(count, counter_dict[char]//ballon_dict[char])
        return count
        
   