class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_end = 0
        curr_far = 0
        jumps = 0
        for i in range(len(nums)-1):
            curr_far = max(curr_far, nums[i]+i)
            if i == curr_end:
                jumps += 1
                curr_end = curr_far
        return jumps
