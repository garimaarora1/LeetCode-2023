class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_cons_length = 0
        
        for num in nums_set:
            if num-1 not in nums_set:
                curr_length = 1
                while num + 1 in nums_set:
                    curr_length += 1
                    num = num + 1
                max_cons_length = max(max_cons_length, curr_length)
        return max_cons_length