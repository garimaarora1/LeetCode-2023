class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        operations = 0
        for val in counter.values():
            if val == 1:
                return -1
            operations += ceil(val/3)
        return operations