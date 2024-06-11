class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)
        res = []
        arr2_set = set(arr2)

        for num in arr2:
            for i in range(counter[num]):
                res.append(num)
            counter[num] = 0
        
        res1 = []
        for key, value in counter.items():
            if value != 0:
                for i in range(value):
                    res1.append(key)
        res.extend(sorted(res1))
        return res
                
            
        