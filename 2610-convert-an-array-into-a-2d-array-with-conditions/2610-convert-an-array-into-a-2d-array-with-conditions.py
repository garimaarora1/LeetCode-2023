class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1
        
        maxi = max(freq_dict.values())
        for i in range(1, maxi+1):
            sub_array = []
            for key, value in freq_dict.items():
                if value >= i:
                    sub_array.append(key)
            res.append(sub_array)
        return res
