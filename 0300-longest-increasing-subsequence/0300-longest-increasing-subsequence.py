class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # finds the leftmost position in the dp where target can be inserted while keeping dp sorted.
        def binary_search(left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if dp[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        dp = []

        for num in nums:
            i = binary_search(0, len(dp) - 1, num)

            if i == len(dp):
                dp.append(num)
            else:
                dp[i] = num
        # note: dp does not contian the Longest Increasing Subsequence
        # dp[1] is the smallest end element of an increasing subsequence of length 2, and so on.
        return len(dp)
