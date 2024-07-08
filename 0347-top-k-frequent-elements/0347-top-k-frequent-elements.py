class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for i in nums:
            counter[i] += 1
        
        res = []
        heap = []
        for key, value in counter.items():
            heappush(heap,(value, key))
            if len(heap) > k:
                heappop(heap) 

        while k > 0:
            v, element = heappop(heap)  
            res.append(element) 
            k -= 1    
        return res            



        
            
        