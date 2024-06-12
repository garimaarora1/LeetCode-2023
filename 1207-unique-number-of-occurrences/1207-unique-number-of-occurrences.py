class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        
        values_set = set()
        for val in counter.values():
            values_set.add(val)
        return len(values_set) == len(counter)