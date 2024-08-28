class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = defaultdict(list)
        for word in strs:
            freq_array = [0] * 26
            for ch in word:
                freq_array[ord(ch)-97] += 1
            freq_map[tuple(freq_array)].append(word)
        return freq_map.values()