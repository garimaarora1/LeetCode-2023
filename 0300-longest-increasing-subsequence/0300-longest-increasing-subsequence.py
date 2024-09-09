class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def bisect_left(dp, target):
            left, right = 0, len(dp)

            # Binary search
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return left
        dp = []

        for num in nums:
            # Use custom bisect_left to find the correct position
            i = bisect_left(dp, num)

            # If num is larger than any element in dp, append it
            if i == len(dp):
                dp.append(num)
            else:
                # Otherwise, replace the element at the found index
                dp[i] = num

        # The length of dp is the length of the longest increasing subsequence
        return len(dp)