class Solution:
    def two_sum(self, nums, target):
        first, second = 0, len(nums)-1
        res = []
        while first < second:
            curr_sum = nums[first] + nums[second]
            if curr_sum == target:
                res.append([nums[first], nums[second]])
                first += 1
                second -= 1
                while first < second and nums[first] == nums[first-1]:
                    first += 1
                while first < second and nums[second] == nums[second+1]:
                    second -= 1
            elif curr_sum < target:
                first += 1
            else:
                second -= 1
        return res
                    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i, val in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = -nums[i]
            two_sum_result = self.two_sum(nums[i+1:], target)
            for res in two_sum_result:
                ans.append([nums[i]] + res)
        return ans
        