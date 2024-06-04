class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        maxi = 0
        curr_sum = 0 
        seen = set()
        while j < len(nums):
            while nums[j] in seen:
                seen.remove(nums[i])
                curr_sum -= nums[i]
                i += 1
            seen.add(nums[j])
            curr_sum += nums[j]
            if j-i+1 == k:
                maxi = max(maxi, curr_sum)
                seen.remove(nums[i])
                curr_sum -= nums[i]
                i += 1 

            j += 1
        return maxi
        
                
        