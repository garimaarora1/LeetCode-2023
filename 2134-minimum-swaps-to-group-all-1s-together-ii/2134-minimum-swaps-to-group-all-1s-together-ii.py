class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        n = len(nums)
        totalOnes = sum(nums)

        if totalOnes == 0:
            return 0

        # Initialize onesCount in the first window
        onesCount = sum(nums[:totalOnes])
        minSwaps = totalOnes - onesCount

        # Sliding window approach
        for start in range(1, n):
            end = (start + totalOnes - 1) % n
            onesCount -= nums[start - 1]
            onesCount += nums[end]
            minSwaps = min(minSwaps, totalOnes - onesCount)

        return minSwaps