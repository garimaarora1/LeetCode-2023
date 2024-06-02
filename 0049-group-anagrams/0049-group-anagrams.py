class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for word in strs:
            freq_array = [0] * 26
            for char in word:
                freq_array[ord(char)-97] += 1
            anagram_dict[tuple(freq_array)].append(word)
        return anagram_dict.values()