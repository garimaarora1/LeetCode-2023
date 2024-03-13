class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        freq_array = [0] * (len(nums))
        ans = []
        for i in range(len(nums)):
            freq_array[nums[i]-1] += 1
        for i in range(len(freq_array)):
            if freq_array[i] == 0:
                ans.append(i+1)
        return ans