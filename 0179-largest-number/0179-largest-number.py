from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def func(second, first):
            if second+first > first+second:
                return -1
            return 1
        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(func))
        return ''.join(nums).lstrip("0") or "0"