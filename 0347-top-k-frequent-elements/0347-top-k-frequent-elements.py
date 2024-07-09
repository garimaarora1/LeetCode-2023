class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        buckets = [[] for _ in range(len(nums)+1)]
        
        counter = Counter(nums)
        
        for key, freq in counter.items():
            buckets[freq].append(key)
        
        flat_list = [item for sublist in buckets for item in sublist]
        
        return flat_list[::-1][:k]



        
            
        