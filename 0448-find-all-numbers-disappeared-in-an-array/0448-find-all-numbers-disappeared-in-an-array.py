class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        freq_array = [0] * (len(nums)+1)
        ans = []
        for i in range(len(nums)):
            freq_array[nums[i]] += 1
        for i in range(1, len(freq_array)):
            if freq_array[i] == 0:
                ans.append(i)
        return ans