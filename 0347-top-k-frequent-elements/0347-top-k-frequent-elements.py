class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        counter = Counter(nums)
        for num, freq in counter.items():
            buckets[freq].append(num)
        
        top_k_freq_elements = []
        
        for bucket in buckets[::-1]:
            for num in bucket:
                top_k_freq_elements.append(num)
                if len(top_k_freq_elements) == k:
                    return top_k_freq_elements