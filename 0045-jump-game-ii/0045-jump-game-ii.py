class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_end, curr_far = 0, 0
        jump = 0
        for i in range(len(nums)-1):
            curr_far = max(curr_far, nums[i] + i)
            if i == curr_end:
                jump += 1
                curr_end = curr_far
        return jump