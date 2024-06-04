class Solution:
    def numberOfWays(self, s: str) -> int:
        """
        Good explanation: https://leetcode.com/problems/number-of-ways-to-select-buildings/discuss/1907179/JavaPython-3-One-pass-S-O(1)-T-O(n)-codes-and-follow-up-w-brief-explanation-and-analysis.
        """
        one, zero, one_zero, zero_one = 0,0,0,0
        total_count = 0
        for ch in s:
            if ch == '0':
                zero += 1
                one_zero += one
                total_count += zero_one
            else:
                one += 1
                zero_one += zero
                total_count += one_zero
        return total_count
        