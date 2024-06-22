class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        queue_size = 0
        count = 0
        initial_gap = 0
        while j <= len(nums) - 1:
            if nums[j] % 2 == 1:
                queue_size += 1

            if queue_size == k:
                initial_gap = 0
                while queue_size == k:
                    queue_size -= (nums[i] % 2)
                    initial_gap += 1 
                    i += 1
            
            count += initial_gap
            j += 1

        return count