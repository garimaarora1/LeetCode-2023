class Solution:
    def nextGreaterElements(self, nums):
        res = [-1] * len(nums)
        stack = []
        for i in range(2 * len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i % len(nums)]:
                stack.pop()
            if stack:
                res[i % len(nums)] = nums[stack[-1]]  
            stack.append(i % len(nums))
        return res
