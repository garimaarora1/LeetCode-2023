class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # hash map and prefix sum
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        curr_sum = 0
        count = 0
        
        for num in nums:
            curr_sum += num
            # what can we chop off from existing array to make it equal to k 
            diff = curr_sum - k
            count += prefix_sum[diff]
            prefix_sum[curr_sum] += 1
        return count