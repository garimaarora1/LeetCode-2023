class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        """
        Approch 1: sorting, TC: nlogn
        1. sort nums, count = 0
        2. whenever nums[i-1] >= nums[i]:
        3. count += nums[i-1]-nums[i] + 1
        4. nums[i]= nums[i-1] + 1
        
        Approach 2: freq array, TC: O(N)
        1. freq array 
        2. len of freq array = len(nums) + max(nums)
        3. count = 0
        4. populate freq array with freqs 
        5. iterate over the freq array and whereever you find duplicate: find no. of duplicates, add duplicates to next ele freq and make current freq = 1, make count += dups
        """
    
        freq_array = [0]*(len(nums) + max(nums) + 1)
        count = 0
        for i in range(len(nums)):
            freq_array[nums[i]] += 1
        
        for i in range(len(freq_array)):
            if freq_array[i] >= 1:
                duplicates = freq_array[i] - 1
                freq_array[i+1] += duplicates
                freq_array[i] = 1
                count += duplicates
                
        return count