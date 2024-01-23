class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        maxi = -1
        counter_dict = defaultdict(int)
        for n in nums:
            counter_dict[n] += 1
        for number in counter_dict:
            value = counter_dict[number]
            if value == 1:
                maxi = max(maxi, number)
        return maxi
        