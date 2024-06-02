class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum and hash map 
        
        d = defaultdict(int)
        d[0] = 1
        curr_sum = 0
        res = 0
        for num in nums:
            curr_sum += num
            if curr_sum - k in d:
                res+= d[curr_sum-k]
            d[curr_sum] += 1
        return res
        