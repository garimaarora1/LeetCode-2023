class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}
        for i in range(len(nums)):
            if nums[i] in idx_map:
                return idx_map[nums[i]], i
            else:
                idx_map[target-nums[i]] = i