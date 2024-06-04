class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        maxi = 0
        while j <= len(nums) - 1:
            if nums[j] == 0:
                k-=1
            if k >= 0:
                maxi = max(maxi, j-i+1)
            while k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
            j += 1
        return maxi