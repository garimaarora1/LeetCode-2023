class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum and hash map 
        prefix_hash_map = defaultdict(int)
        prefix_hash_map[0] = 1
        curr_prefix_sum = 0
        count = 0
        for i in range(len(nums)):
            curr_prefix_sum += nums[i]
            if curr_prefix_sum - k in prefix_hash_map:
                count += prefix_hash_map[curr_prefix_sum - k]
            prefix_hash_map[curr_prefix_sum] += 1 
        return count