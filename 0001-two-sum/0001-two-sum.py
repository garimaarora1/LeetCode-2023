class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in h_map:
                return i, h_map[nums[i]]
            else:
                h_map[target-nums[i]] = i