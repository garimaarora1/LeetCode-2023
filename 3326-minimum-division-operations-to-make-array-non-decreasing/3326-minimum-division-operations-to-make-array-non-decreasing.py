class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                nums[i - 1] = self.findDivisor(nums[i], nums[i - 1])
                if nums[i - 1] == -1: return -1
                ans += 1
        return ans
    
    def findDivisor(self, smaller, larger):
        for divisor in range(2, smaller + 1):
            if larger % divisor == 0:
                return divisor
        return -1