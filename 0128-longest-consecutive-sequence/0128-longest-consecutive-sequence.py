class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxi = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                curr_length = 1
                while (num + curr_length) in nums_set:
                    curr_length += 1
                maxi = max(maxi, curr_length)
        return maxi